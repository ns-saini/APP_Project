from lib.math_lib import *
from lib.root_approximation import *
from lib.trignometry import*


radius = float(input("Enter the radius: "))

root_wbi = RootApproximation_WBI()
twbi = TrignometryWBI(precision=4)
f_wbi = lambda x: x ** 2 + twbi.sin(x) - 2
alpha = root_wbi.get_roots(f_wbi, 0.00001)
alpha = calculate_pi()/2 + twbi.sin(alpha[0])

# sine_value = twbi.sin()
print("Alpha with WBI is ", alpha)
length = 2 * radius * (1 - twbi.cos(alpha/2))

print("The length with WBI is :" + str(length))


root_bi = RootApproximation_BI()
tbi = TrignometryBI(precision=4)
f_bi = lambda x: x ** 2 + tbi.sin(x) - 2
alpha = root_bi.get_roots(f_bi, 0.00001)
alpha = calculate_pi()/2 + tbi.sin(alpha[0])

# sine_value = twbi.sin()
print("Alpha with BI is ", alpha)

length = 2 * radius * (1 - tbi.cos(alpha/2))

print("The length with BI is :" + str(length))
