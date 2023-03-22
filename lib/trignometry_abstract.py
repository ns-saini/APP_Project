"""Module providing Abstract Base classes for python."""
from abc import ABC, abstractmethod

class Trignometry(ABC):
    """Abstract Base Class for Trignometry provides sin and cos methods."""

    @abstractmethod
    def sin(self, rad: float) -> float:
        """Abstract method for sin."""

    @abstractmethod
    def cos(self, rad: float) -> float:
        """Abstract method for cos."""
