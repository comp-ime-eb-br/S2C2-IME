from threading import Thread
import json
from .constants import MininetConstants

class OutputHandler:
    def __init__(self, content, notifier):
        self.notifier = notifier
        self.eventType = "default"
        self.formattedContent(content)

    def process(self):
        self.notifier.notify({"type": self.eventType, "value": self.contents})

    def formattedContent(self, content):
        splittedContent = content.decode('utf-8').replace("\'", "\"").split("\n")

        self.contents = []
        for c in splittedContent:
            self.contents.append(json.loads(c))

class EOFHandler(OutputHandler):
    def __init__(self, content, notifier):
        pass

    def process(self):
        pass

class PartialResultHandler(OutputHandler):
    def __init__(self, content, notifier):
      super().__init__(content, notifier)
      self.eventType = MininetConstants.UPDATE


class ErrorHandler(OutputHandler):
    def __init__(self, content, notifier):
      super().__init__(content, notifier)
      self.eventType = MininetConstants.ERROR