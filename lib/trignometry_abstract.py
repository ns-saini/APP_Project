from abc import ABC, abstractmethod


class Trignometry(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def sin(self, rad):
        pass
