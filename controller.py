"""
    Controller module
"""
from lib import math_lib
from lib import root_approximation
from lib import trignometry


class Controller:
    """
    Controller class for calculating the length of the chord between the two circles of radius r
    """
    def __init__(self):
        self.temp = 0

    @staticmethod
    def calculate_length_wbi(radius):
        """
        calculate_length_WBI method for calculating length without Builtin functions
        """

        rootapprox_wb = root_approximation.RootApproximationWBI()
        trigo_wb = trignometry.TrignometryBI(precision=4)
        maths_wb = math_lib.MathLibWBI()

        def funct_wb(var_x):
            temp_val = var_x ** 2
            return temp_val + trigo_wb.sin(var_x) - 2
        alpha = rootapprox_wb.get_roots(funct_wb, 0.00001)
        alpha = maths_wb.get_pi()/2 + trigo_wb.sin(alpha[0])
        length = 2 * radius * (1 - trigo_wb.cos(alpha/2))
        print("(INCARNATION 1) The length without BI is :" + str(length))
        return length

    @staticmethod
    def calculate_length_bi(radius):
        """
        calculate_length_BI method for calculating length with Builtin functions
        """

        rootapprox_b = root_approximation.RootApproximationBI()
        maths_b = math_lib.MathLibBI()
        trigo_b = trignometry.TrignometryBI(precision=4)

        def funct_b(var_x):
            temp_val = var_x ** 2
            return temp_val + trigo_b.sin(var_x) - 2
        alpha = rootapprox_b.get_roots(funct_b, 0.00001)
        alpha = maths_b.get_pi()/2 + trigo_b.sin(alpha[0])
        length = 2 * radius * (1 - trigo_b.cos(alpha/2))
        print("(INCARNATION 2) The length with BI is :" + str(length))
        return length
