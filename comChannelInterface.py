from abc import ABC, abstractmethod


class CommunicationChannel(ABC):

    @abstractmethod
    def send_message(self, title=None, body='', number=None, email=None):
        pass
