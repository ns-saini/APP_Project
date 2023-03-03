from abc import ABC, abstractmethod

class MathLib(ABC):
    def __init__(self, precision) -> None:
        self.precision = precision
        super().__init__()

    @abstractmethod
    def exp(self, number: float, power:int) -> float:
        pass

    @abstractmethod
    def factorial(self, numeber: int) -> int:
        pass

    @abstractmethod
    def get_pi(self) -> float:
        pass