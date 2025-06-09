from pexpect import popen_spawn, EOF
from signal import SIGCHLD
import subprocess
import json
import time
from .outputHandler import PartialResultHandler, ErrorHandler, EOFHandler
from .constants import MininetConstants
class MininetWifiExp():
    RUN_CMD = 'sudo python3 -u mininetWifiAdapter/MininetScript.py'
    CLEAR_CMD= 'sudo mn -c && sudo service network-manager restart && sudo sync && sudo sysctl vm.drop_caches=3'
    KILL_CMD = 'sudo kill -9 && sudo service network-manager restart && sudo sync && sudo sysctl vm.drop_caches=3'
    EXPERIMENT_TIMEOUT = 125
    PROCESS_OFFSET = 2

    OUTPUT_PATTERNS = [
        r'(\{\'time\':\s+[0-9]+\,\s+\'positions\':\s+\{(\'.+\':\s+\{\'type\':\s+\'.+\',\s+\'position\':\s+\[.*\]\})*\}\})',
        r'(\{\'time\':\s+[0-9]+\,\s+\'radioFrequency\':\s+\[\{.*\}\]\})',
        r'(\{\'time\':\s+[0-9]+\,\s+\'performance\':\s+\{.*\}\})',
        r'(\{\'error\':\s+\'.*\'\})', 
        EOF
    ]
    OUTPUT_STRATEGY_MAPPING = [PartialResultHandler, PartialResultHandler, PartialResultHandler, ErrorHandler, EOFHandler]
    
    def __init__(self, notifier, configuration):
        self.__notifier = notifier
        self.__active = False
        self.__process = None
        self.__start = 0
        self._configuration = configuration

    def run(self):
        self.__notifier.notify({"type": MininetConstants.START, "value": ""})
        self.__serializeConfiguration()
        self.__active = True
        self.__process = popen_spawn.PopenSpawn(self.RUN_CMD)
        self.__start = time.time()
        
        while self.__shouldKeepRunning():
            if self.__isTimeExpired():
                self.finish()

            if self.__process is None:
                break

            index = self.__process.expect(self.OUTPUT_PATTERNS)
            outputHandler = self.OUTPUT_STRATEGY_MAPPING[index](self.__process.after, self.__notifier)
            outputHandler.process()

    def __serializeConfiguration(self):
        with open(MininetConstants.CONFIG_FILE_PATH, 'w') as outfile:
            jsonString = json.dumps(self._configuration, default=lambda o: o.__dict__)
            json.dump(jsonString, outfile)
            outfile.close()

    def __isTimeExpired(self):
        currentTime = time.time()
        duration = currentTime - self.__start
        return duration > self.EXPERIMENT_TIMEOUT


    def __shouldKeepRunning(self):
        return self.__active


    def finish(self):
        self.__active = False
        self.__start = 0

        if self.__process:
            cmd = "{} {}".format(self.KILL_CMD, str(self.__process.pid + self.PROCESS_OFFSET))
            subprocess.run(cmd, shell=True)
            subprocess.run(self.CLEAR_CMD, shell=True)
            
        self.__notifier.notify({"type": MininetConstants.FINISH, "value": ""})

    def addListener(self, listener):
        self.__notifier.attach(listener)