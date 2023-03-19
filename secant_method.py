from lib.trignometry import TrignometryWBI
from lib.math_lib import MathLib_WBI

R = float(input("Enter the radius: "))
twbi = TrignometryWBI()
mwbi = MathLib_WBI()

def f(alpha):
    return alpha - twbi.sin(alpha) - mwbi.get_pi()/2


def f_alpha():
    a = mwbi.get_pi()/4  
    b = a + 0.01  
    tol = 1e-8  # tolerance
    max_iterations = 1000  
    for i in range(max_iterations):
        c = b - f(b)*(b - a)/(f(b) - f(a))
        if abs(c - b) < tol:
            return c
        a = b
        b = c
    raise Exception("Failed to converge")

alpha = f_alpha()

print("The value of alpha is: ", alpha)

# Calculate the length of the segment X1X2
l = 2*R*(1 - twbi.cos(alpha/2))
print("The length of segment is: ", l)

print(f"The two coasters need to be moved {l:.4f} units on top of each other.")