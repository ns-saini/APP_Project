"""
    Controller module
"""
from lib import math_lib
from lib import root_approximation
from lib import trignometry
from lib import input_validator
from lib import output_xml_generator


class Controller:
    """
    Controller class    
    """
    
    def __init__(self, radius):
        #pass
        # global rad
        
        if radius <= 0:
            raise ValueError("Radius must be a positive number")
        
        self.radius = radius
        # rad = self.radius

        # # self.radius = float(input("Enter the radius: "))

        # if self.radius <= 0:
        #     raise ValueError("Radius must be positive")


    def calculate_length_wbi(self, radius):
        """
        calculate_length_WBI    
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
        print("The length with WBI is :" + str(length))
        return length


    def calculate_length_bi(self, radius):
        """
        calculate_length_BI    
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
        print("The length with BI is :" + str(length))
        return length


#radius = float(input_validator.validate_input())
#controller = Controller(radius)

