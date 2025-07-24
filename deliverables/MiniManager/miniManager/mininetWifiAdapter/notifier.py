import asyncio
from abc import ABC, abstractmethod
from threading import Thread

class IResultEventListener(ABC):
    @abstractmethod
    def update(self, subject):
        pass
class ResultNotifier():

    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def __notify(self, subject):
        for observer in self._observers:
            observer.update(subject)

    def notify(self, subject):
        thread = Thread(target=self.__notify, args=(subject,))
        thread.daemon = True
        thread.start()
