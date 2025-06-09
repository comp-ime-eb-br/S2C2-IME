import time
import json
import threading

from mininet.log import setLogLevel

import constants
import measurers as meas
import decorators

class MininetScript():
    ERROR_CONFIG = "error opening configurations"
    DELAY = 1

    def __init__(self):
        self.__configuration = self.__loadConfiguration()
        self.__radioFrequencyMeasurements = self.__configuration["radioFrequencyMeasurements"]
        self.__performanceMeasurements = self.__configuration["performanceMeasurements"]
        self.__net = None

    def __loadConfiguration(self):
        try:
            outfile = open(constants.MininetConstants.CONFIG_FILE_PATH, 'r')
            data = outfile.read()
            outfile.close()

            jsonParsed = json.loads(data)
            return json.loads(jsonParsed)
        except:
            print({constants.MininetConstants.ERROR_KEY: self.ERROR_CONFIG})

    def run(self):
        self.__start = time.time()
        self.__topology()
        self.__analyse()

    def __topology(self):
        networkAttributes = self.__configuration["network"]["args"]
        isAdhoc = self.__configuration["network"]["adhoc"]
        mininetNetwork = decorators.MininetNetwork(networkAttributes, self.__configuration["nodes"], isAdhoc)
        propagationModel = decorators.PropagationModelDecorator(mininetNetwork, self.__configuration["propagationModel"])
        mobilityModel = decorators.MobilityModelDecorator(propagationModel, self.__configuration["mobilityModel"])
        networkStarter = decorators.NetworkStarterDecorator(mobilityModel, self.__configuration["links"], isAdhoc)
        
        networkStarter.configure()
        self.__net = networkStarter.getNetwork()

    def __analyse(self):
        nodes = { "station": self.__net.stations, "accessPoint": self.__net.aps }
        positionMeasurer = meas.PositionMeasurer(self.__start, nodes)
        radioFrequencyMeasurer = meas.RadioFrequencyMeasurer(self.__start, self.__net.stations, self.__radioFrequencyMeasurements)
        performanceMeasurer = meas.PerformanceMeasurer(self.__start, self.__net, self.__performanceMeasurements)

        measurers = [positionMeasurer, radioFrequencyMeasurer, performanceMeasurer]

        threads = []
        for measurer in measurers:
            t = threading.Thread(target=measurer.run)
            t.daemon = True
            t.start()
            threads.append(t)

        for t in threads:
            t.join()

if __name__ == '__main__':
    setLogLevel('info')
    script = MininetScript()
    script.run()