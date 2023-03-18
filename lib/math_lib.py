from lib.math_lib_abstract import MathLib as ML
import math


def calculate_pi():
    val = 0.0
    total_terms = 100
    for i in range(1, 2 * total_terms, 2):
        sign = -(i % 4 - 2)
        val += float(sign) / i
    return 4 * val


class MathLib_BI(ML):
    def __init__(self) -> None:
        super().__init__(4)

    def pow(self, number: float, power: int) -> float:
        return math.pow(number, power)

    def factorial(self, number: int) -> int:
        return math.factorial(number)

    def get_pi(self) -> float:
        return math.pi


class MathLib_WBI(ML):
    def __init__(self):
        self.PI = None

    def pow(self, number: float, power: int) -> float:
        if power == 0:
            return 1
        elif power % 2 == 0:
            temp = pow(number, power // 2) 
            return temp * temp
        else:
            return number * pow(number, power - 1)

    def factorial(self, num: int) -> int:
        if num < 0:
            raise ValueError("Factorial can't be calculated for negative numbers")
        result = 1
        for i in range(1, num + 1):
            result *= i
        return result

    def get_pi(self):
        if self.PI is not None:
            return self.PI
        return calculate_pi()


