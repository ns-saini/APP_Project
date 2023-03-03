"""
Method for Sin,
The sin method is explored further with McLaurin Series.
Reference: https://blogs.ubc.ca/infiniteseriesmodule/units/unit-3-power-series/taylor-series/maclaurin-expansion-of-sinx/
The number of iterations are equal to number of precisions. Block number for number of precision
"""
from lib.math_lib import MathLib


class Trignometry:
    def __init__(self, m_lib: MathLib, precision=4):
        self.precision = precision
        self.m_lib = m_lib

    def sin(self, rad):
        total_iterations = self.precision
        result = 0
        for i in range(1, total_iterations):
            result += (self.m_lib.exp(-1, i) * self.m_lib.exp(rad, 2 * i + 1))/self.m_lib.factorial(2 * i + 1)

        print(result)
        return result



