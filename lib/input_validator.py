'''
    Module to validate user input
'''

def validate_input():
    """
    Prompts the user to enter values for the tolerance, initial guess x0, and
    initial guess x1 for the numerical root-finding method.

    Returns a tuple containing the validated values for tol, x0, and x1.

    Raises:
    -------
    ValueError: If the tolerance value entered is non-positive, or if any of
                the input values cannot be converted to a float.
    """
    # while True:
    #     try:
    #         tol = float(input("Please enter a value for the tolerance (e.g. 0.0001): "))
    #         if tol <= 0:
    #             raise ValueError
    #         break
    #     except ValueError:
    #         print("Invalid input. Please enter a positive number.")

    # while True:
    #     try:
    #         x0 = float(input("Please enter a value for the initial guess x0: "))
    #         break
    #     except ValueError:
    #         print("Invalid input. Please enter a number.")

    # while True:
    #     try:
    #         x1 = float(input("Please enter a value for the initial guess x1: "))
    #         break
    #     except ValueError:
    #         print("Invalid input. Please enter a number.")

    # return tol, x0, x1

    while True:
        try:
            radius = float(input("Please enter a value for the radius of the coaster (e.g. 20): "))
            if radius <= 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter a positive number.")
    return radius
