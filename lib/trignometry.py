"""
Method for Sin,
The sin method is explored further with McLaurin Series.
Reference: https://blogs.ubc.ca/infiniteseriesmodule/units/unit-3-power-series/taylor-series/maclaurin-expansion-of-sinx/
The number of iterations are equal to number of precisions. Block number for number of precision



"""
from lib.math_lib import MathLib


class Trignometry:
    def __init__(self, m_lib: MathLib, precision=4):
        """
        Initializes an instance of the Trignometry class with a specified MathLib object and precision value.

        Args:
        - m_lib: the MathLib object to be used for calculations
        - precision: the number of iterations to be performed in the calculation (default is 4)
        """
        self.precision = precision
        self.m_lib = m_lib

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
        for i in range(1, total_iterations):
            result += (self.m_lib.exp(-1, i) * self.m_lib.exp(rad, 2 * i + 1))/self.m_lib.factorial(2 * i + 1)

        print(result)
        return result
         



