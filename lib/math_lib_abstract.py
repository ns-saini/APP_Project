"""MathLib abstract class."""
from abc import ABC, abstractmethod


class MathLib(ABC):
    """Abstract Base Class for MathLib provides pow, factorial, and get_pi methods."""
    def __init__(self, precision) -> None:
        self.precision = precision

    @abstractmethod
    def pow(self, number: float, power: int) -> float:
        """Abstract method for pow."""

    @abstractmethod
    def factorial(self, number: int) -> int:
        """Abstract method for factorial."""

    @abstractmethod
    def get_pi(self) -> float:
        """ Abstract method for get_pi."""
