from lib.trignometry import TrignometryWBI
from lib.math_lib import MathLib_WBI

R = float(input("Enter the radius: "))
twbi = TrignometryWBI()
mwbi = MathLib_WBI()

# Function for ALPHA
def find_alpha():
    """
    Find the value of alpha that satisfies the equation alpha - sin(alpha) = pi/2.
    """
    def g(alpha):
       return alpha - twbi.sin(alpha) - mwbi.get_pi()/2 

    def g_prime(alpha):
        twbi = TrignometryWBI()
        return 1 - twbi.cos(alpha)

    alpha = 1  # initial guess
    tol = 1e-6
    max_iters = 100

    for i in range(max_iters):
        f_alpha = g(alpha)
        f_prime_alpha = g_prime(alpha)
        alpha_next = alpha - f_alpha / f_prime_alpha
        if abs(alpha_next - alpha) < tol:
            return alpha_next
        alpha = alpha_next

    raise ValueError("Maximum iterations exceeded without convergence.")

# Find the value of alpha that satisfies the equation alpha - sin(alpha) = pi/2
alpha = find_alpha()
print("The value of alpha that satisfies the equation is:", alpha)

# Calculate the length l of the overlapping segment
  # assume radius of each coaster is 1 (they have equal area)
l = 2 * R * (1 - twbi.cos(alpha/2))
print("The length of the overlapping segment is:", l)