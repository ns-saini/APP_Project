from lib.math_lib import calculate_pi
from lib.trignometry import *



def angle_alpha():

    """
    alpha - sin(alpha) = pi/2
    """

    def f(alpha):
        twbi = TrignometryWBI()
        mwbi = MathLib_WBI()
        return alpha - twbi.sin(alpha) - mwbi.get_pi()/2


    def f_derivative(alpha):
        twbi = TrignometryWBI()
        return 1 - twbi.cos(alpha)

    alpha = 1  
    tol = 1e-6
    maximum_iterations = 100

    for i in range(maximum_iterations):
        f_alpha = f(alpha)
        f_derivative_alpha = f_derivative(alpha)
        alpha_next = alpha - f_alpha / f_derivative_alpha
        if abs(alpha_next - alpha) < tol:
            return alpha_next
        alpha = alpha_next

    raise ValueError("Maximum iterations exceeded without convergence.")

# Find the value of alpha that satisfies the equation alpha - sin(alpha) = pi/2
alpha = angle_alpha()
print("The value of alpha that satisfies the equation is:", alpha)
