from lib.math_lib import MathLib
from lib.trignometry import Trignometry



def angle_alpha():

    """
    alpha - sin(alpha) = pi/2
    """

    def f(alpha):
        return alpha - Trignometry.sin(alpha) - MathLib.get_pi/2
    

    def f_derivative(alpha):
        return 1 - Trignometry.cos(alpha)

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
