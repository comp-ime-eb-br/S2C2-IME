from asyncio import run
from mininetWifiAdapter import IResultEventListener
from .webSocketServer import WebSocketServer
from .experimentsQueue import ExperimentsQueue
from .models import Round


class ExperimentListener(IResultEventListener):
    def __init__(self, roundID):
        self.__roundID = roundID
        self.__started = False

    def update(self, subject):
        run(self.__sendMessage(subject))

        if subject["type"] == "UPDATE" and self.__started == False:
            self.__started = True
            self.__updateStatus(Round.IN_PROGRESS)

        if subject["type"] == "FINISH":
            self.__updateStatus(Round.DONE)
            ExperimentsQueue.instance().experimentFinished(self.__roundID)

    def __updateStatus(self, status):
        round = Round.objects.get(id=self.__roundID)
        round.status = status
        round.save()


    async def __sendMessage(self, subject):
        await WebSocketServer.sendMessageToRoom(self.__roundID, subject)