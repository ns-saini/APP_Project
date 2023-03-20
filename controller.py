from lib.math_lib import *
from lib.root_approximation import *
from lib.trignometry import*


radius = float(input("Enter the radius: "))

rootapprox_wb = RootApproximation_WBI()
trigo_wb = TrignometryWBI(precision=4)
maths_wb=MathLib_WBI()
funct_wb = lambda x: x ** 2 + trigo_wb.sin(x) - 2
alpha = rootapprox_wb.get_roots(funct_wb, 0.00001)
alpha = maths_wb.get_pi()/2 + trigo_wb.sin(alpha[0])

# sine_value = trigo_wb.sin()

length = 2 * radius * (1 - trigo_wb.cos(alpha/2))
print("The length with WBI is :" + str(length))


root_b = RootApproximation_BI()
maths_b = MathLib_BI()
trigo_b = TrignometryBI(precision=4)
funct_b = lambda x: x ** 2 + trigo_b.sin(x) - 2
alpha = root_b.get_roots(funct_b, 0.00001)
alpha = maths_b.get_pi()/2 + trigo_b.sin(alpha[0])

# sine_value = trigo_wb.sin()

length = 2 * radius * (1 - trigo_b.cos(alpha/2))
print("The length with BI is :" + str(length))