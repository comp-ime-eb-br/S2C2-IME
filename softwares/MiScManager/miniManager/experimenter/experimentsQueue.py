import threading
from queue import Queue
import time
from provenanceCatcher import ProvenanceManager, ProvenanceListener
from .models import Round

class ExperimentsQueue:

    _instance = None
    POLLING_PERIOD = 2

    def __init__(self):
        self.queue = Queue()
        self.__busy = False
        self.__roundToExperimentMap = {}
        self.__currentRound = 0

        t = threading.Thread(target=self._consume)
        t.daemon = True
        t.start()


    def add(self, mininetWifiExp, roundID, medicao_schema):
        self.__roundToExperimentMap[str(roundID)] = { "experiment": mininetWifiExp, "medicao_schema": medicao_schema }
        self.queue.put(roundID)

    def finishExperiment(self, roundID):
        key = str(roundID)
        if not (key in self.__roundToExperimentMap):
            return
        
        experiment = self.__roundToExperimentMap[key]["experiment"]
        del self.__roundToExperimentMap[key]
        experiment.finish()

    def experimentFinished(self, roundID):
        if roundID == self.__currentRound:
            self.__busy = False

    def _consume(self):
        while True:
            time.sleep(self.POLLING_PERIOD)
            if self.__busy or self.queue.empty():
                continue

            self.__busy = True
            roundID = self.queue.get()
            if not (str(roundID) in self.__roundToExperimentMap):
                continue

            self.__startExperiment(roundID);

    def __startExperiment(self, roundID):
        self.__currentRound = roundID
        element = self.__roundToExperimentMap[str(roundID)]
        self.__updateRoundStatus(roundID)
        self.__startCapture(roundID, element["medicao_schema"])
        experiment = element["experiment"]
        experiment.addListener(ProvenanceListener())
        element["experiment"].run()

    def __updateRoundStatus(self, roundID):
        round = Round.objects.get(id=roundID)
        round.status = Round.STARTING
        round.save()

    def __startCapture(self, roundID, schema):
        provenanceCatcher = ProvenanceManager.instance()
        provenanceCatcher.reset(roundID, schema)

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance