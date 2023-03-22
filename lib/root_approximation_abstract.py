"""Abstract class for root approximation methods."""
from abc import ABC, abstractmethod


class RootApproximation(ABC):
    """Abstract Base Class for RootApproximation provides get_roots method."""
    def __init__(self) -> None:
        """ Initializes an instance of the RootApproximation class with a
        default value of 100 for the number of terms."""
        self.num_terms = 100
        super().__init__()

    @abstractmethod
    def get_roots(self, func, error) -> list:
        """Abstract method for get_roots."""
