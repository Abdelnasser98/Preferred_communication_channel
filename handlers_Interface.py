from abc import ABC, abstractmethod


class HandlerInterface(ABC):

    @abstractmethod
    def handler(self):
        pass
