from lib.trignometry import TrignometryWBI
from lib.math_lib import MathLib_WBI

R = float(input("Enter the radius: "))
twbi = TrignometryWBI()
mwbi = MathLib_WBI()


def f_value(alpha):
    return alpha - twbi.sin(alpha) - mwbi.get_pi()/2


# BISECTION METHOD

# Use the bisection method to find the value of alpha that solves f(alpha) = 0
a = 0
b = mwbi.get_pi()
tolerance = 1e-6

while b - a > tolerance:
    c = (a + b) / 2
    if f_value(a) * f_value(c) < 0:
        b = c
    else:
        a = c

alpha = (a + b) / 2

# Calculate the length of the segment X1X2

l = 2*R*(1 - twbi.cos(alpha/2))

print("The value of alpha is: ", alpha)

print("The length of segment is: ", l)

# Print the result
print(f"The two coasters need to be moved {l:.4f} units on top of each other.")
