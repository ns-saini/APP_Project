from lib.abstract.math_lib import MathLib as ML
import math

class MathLib(ML):

    def __init__(self, precision) -> None:
        super().__init__(precision)

    def exp(self, number: float, power:int) -> float:
        return math.exp(number, power)
    
    def factorial(self, number: int) -> int:
        return math.factorial(number)

    def get_pi(self) -> float:
        return math.pi