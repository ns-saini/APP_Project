from abc import ABC, abstractmethod


class MathLib(ABC):
    def __init__(self, precision) -> None:
        self.precision = precision

    @abstractmethod
    def pow(self, number: float, power: int) -> float:
        pass

    @abstractmethod
    def factorial(self, number: int) -> int:
        pass

    @abstractmethod
    def get_pi(self) -> float:
        pass
