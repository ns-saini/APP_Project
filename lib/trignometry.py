"""
Method for Sin,
The sin method is explored further with McLaurin Series.
Reference: https://blogs.ubc.ca/infiniteseriesmodule/units/unit-3-power-series/taylor-series/maclaurin-expansion-of-sinx/
The number of iterations are equal to number of precisions. Block number for number of precision
"""
import math

from lib.math_lib import MathLib_BI, MathLib_WBI
from lib.trignometry_abstract import Trignometry as Trig


class TrignometryWBI(Trig):
    def __init__(self, precision=4):
        self.precision = precision
        self.m_lib = MathLib_WBI()

    def sin(self, rad):
        total_iterations = self.precision
        result = 0
        for i in range(0, total_iterations):
            result += (self.m_lib.pow(-1, i) * self.m_lib.pow(rad, (2 * i) + 1)) / self.m_lib.factorial((2 * i) + 1)
        return result

    def cos(self, rad: float) -> float:
        total_iterations = self.precision
        result = 0 
        for i in range(0, total_iterations):
            result += (self.m_lib.pow(-1, i) * self.m_lib.pow(rad, 2 * i)) / self.m_lib.factorial(2 * i)
        return result

class TrignometryBI(Trig):
    def __init__(self, precision=4):
        super().__init__()
        self.precision = precision
        self.m_lib = MathLib_BI()

    def sin(self, rad: float) -> float:
        return math.sin(rad)

    def cos(self, rad: float) -> float:
        return math.cos(rad)