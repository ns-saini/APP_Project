from lib import math_lib
from lib import root_approximation
from lib import trignometry

class Controller:
    def __init__(self, radius):
        self.radius = radius
        # self.radius = float(input("Enter the radius: "))
        
        if self.radius <= 0:
            raise ValueError("Radius must be positive")



    def calculate_length_WBI(self):

        rootapprox_wb = root_approximation.RootApproximationWBI()
        trigo_wb = trignometry.TrignometryBI(precision=4)
        maths_wb=math_lib.MathLibWBI()
        

        
        funct_wb = lambda x: x ** 2 + trigo_wb.sin(x) - 2
        alpha = rootapprox_wb.get_roots(funct_wb, 0.00001)
        alpha = maths_wb.get_pi()/2 + trigo_wb.sin(alpha[0])
        print(alpha)

        # sine_value = trigo_wb.sin()

        length = 2 * self.radius * (1 - trigo_wb.cos(alpha/2))
        print("The length with WBI is :" + str(length))

    def calculate_length_BI(self):


        rootapprox_b = root_approximation.RootApproximationBI()
        maths_b = math_lib.MathLibBI()
        trigo_b = trignometry.TrignometryBI(precision=4)
        funct_b = lambda x: x ** 2 + trigo_b.sin(x) - 2
        alpha = rootapprox_b.get_roots(funct_b, 0.00001)
        alpha = maths_b.get_pi()/2 + trigo_b.sin(alpha[0])

        # sine_value = trigo_b.sin()

        length = 2 * self.radius * (1 - trigo_b.cos(alpha/2))
        print("The length with BI is :" + str(length))
        
radius = float(input("Enter the radius: "))
controller = Controller(radius=radius)
length_wbi = controller.calculate_length_WBI()
length_bi = controller.calculate_length_BI()