"""Math module for inbuilt math functions."""
import math

from lib.math_lib import MathLibBI, MathLibWBI
from lib.trignometry_abstract import Trignometry as Trig


class Trignometry:
    """
     Trignometry class for calculating the sine and cosine of an angle using the Maclaurin series.
    """
    def __init__(self, precision=4):
        """
        Initializes an instance of the Trignometry class with a
        specified MathLib object and precision value.

        Args:
        - m_lib: the MathLib object to be used for calculations
        - precision: the number of iterations to be performed
          in the calculation (default is 4)
        """
        self.precision = precision
        self.m_lib = MathLibWBI()

    def sin(self, rad):
        """
        Calculates the sine of a given angle in radians using the Maclaurin series approximation.

        Args:
        - rad: the angle in radians to be used for the calculation

        Returns:
        - The sine of the given angle calculated using the Maclaurin series approximation.
        """
        total_iterations = self.precision
        result = 0
        for i in range(0, total_iterations):
            result += (self.m_lib.pow(-1, i) * self.m_lib.pow(rad, (2 * i) + 1)) / \
                                                self.m_lib.factorial((2 * i) + 1)
        return result

    def cos(self, rad: float) -> float:
        """
        Calculates the cos of a given angle in radians using the
        McLaurin series with the given precision.

        Args:
            rad (float): The angle in radians.

        Returns:
            float: The cos of the angle.
        """
        total_iterations = self.precision
        result = 0
        for i in range(0, total_iterations):
            result += (self.m_lib.pow(-1, i) * self.m_lib.pow(rad, 2 * i)) / \
                                self.m_lib.factorial(2 * i)
        return result

class TrignometryBI(Trig):
    """
    Trignometry class for calculating the sine and cosine of an angle
      using the built-in `math` library.
    """
    def __init__(self, precision=4):
        """
        Initializes an instance of the TrignometryBI class with a specified precision value."""
        super().__init__()
        self.precision = precision
        self.m_lib = MathLibBI()

    def sin(self, rad: float) -> float:
        """
        Calculates the sin of a given angle in radians using the built-in `math` library.

        Args:
            rad (float): The angle in radians.

        Returns:
            float: The sin of the angle.
        """
        return math.sin(rad)

    def cos(self, rad: float) -> float:
        """
        Calculates the cos of a given angle in radians using the built-in `math` library.

        Args:
            rad (float): The angle in radians.

        Returns:
            float: The cos of the angle.
        """
        return math.cos(rad)
    