'''
    Module to validate user input
'''

def prompt_float_input(prompt):
    """
    Prompts the user to enter a float value.
    Returns:
    -------
    A float value.
    Raises:
    -------
    ValueError: If the input value cannot be converted to a float.
    """
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a number.",)
            

def validate_input():
    """
    Prompts the user to enter a value for the radius of the coaster.
    Returns:
    -------
    A float value for the radius of the coaster.
    Raises:
    -------
    ValueError: If the input value is non-positive.
    """
    while True:   
                radius = prompt_float_input("Please enter a value for the radius of the coaster (e.g. 20): ")
                if radius <= 0:
                    print("Invalid input. The radius must be a positive number.")
                else:
                    return radius
        

