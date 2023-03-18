from abc import ABC, abstractmethod


class RootApproximation(ABC):
    def __init__(self) -> None:
        self.num_terms = 100
        super().__init__()

    @abstractmethod
    def get_roots(self, func, e) -> list:
        pass