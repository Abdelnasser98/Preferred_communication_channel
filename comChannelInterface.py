from abc import ABC, abstractstaticmethod


class CommunicationChannel(ABC):

    @abstractstaticmethod
    def send_message(title=None, body='', number=None, email=None):
        """This is method for the communication channels"""
        pass
