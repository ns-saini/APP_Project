"""Abstract module for math library."""
import math
from lib.math_lib_abstract import MathLib as ML

def calculate_pi():
    """
    Calculates the value of pi using the Leibniz formula.

    Returns:
        float: The value of pi.
    """
    val = 0.0
    total_terms = 1000
    for i in range(1, 2 * total_terms, 2):
        sign = -(i % 4 - 2)
        val += float(sign) / i
    return 4 * val


class MathLibBI(ML):
    """Math Library class using built in functions."""
    def __init__(self) -> None:
        super().__init__(4)

    def pow(self, number: float, power: int) -> float:
        """
        Calculates the power of a given number using the built-in `math` library.

        Args:
            number (float): The number to calculate the power of.
            power (int): The power to raise the number to.

        Returns:
            float: The result of the power operation.
        """
        return math.pow(number, power)

    def factorial(self, number: int) -> int:
        """
        Calculates the factorial of a given number using the built-in `math` library.

        Args:
            number (int): The number to calculate the factorial of.

        Returns:
            int: The result of the factorial operation.
        """
        return math.factorial(number)

    def get_pi(self) -> float:
        """
        Returns the value of pi using the built-in `math` library.

        Returns:
            float: The value of pi.
        """
        return math.pi


class MathLibWBI(ML):
    """Math Library class implementing the methods without using inbuilt libraries."""
    def __init__(self):
        self.pi = None

    def pow(self, number: float, power: int) -> float:
        """
        Calculates the power of a given number using the recursive method.

        Args:
            number (float): The number to calculate the power of.
            power (int): The power to raise the number to.

        Returns:
            float: The result of the power operation.
        """
        if power == 0:
            return 1
        if power % 2 == 0:
            temp = pow(number, power // 2)
            return temp * temp
        return number * pow(number, power - 1)

    def factorial(self, num: int) -> int:
        """
        Calculates the factorial of a given number using the iterative method.

        Args:
            num (int): The number to calculate the factorial of.

    def factorial(self, num):
        """
        if num < 0:
            raise ValueError("Factorial can't be calculated for negative numbers")
        result = 1
        for i in range(1, num + 1):
            result *= i
        return result

    def get_pi(self):
        """
        Calculates the value of pi using the Leibniz formula.

        Returns:
            float: The value of pi.
        """
        if self.pi is not None:
            return self.pi
        return calculate_pi()
    