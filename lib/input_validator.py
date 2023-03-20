def validate_input():
    while True:
        try:
            tol = float(input("Please enter a value for the tolerance (e.g. 0.0001): "))
            if tol <= 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter a positive number.")

    while True:
        try:
            x0 = float(input("Please enter a value for the initial guess x0: "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    while True:
        try:
            x1 = float(input("Please enter a value for the initial guess x1: "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    return tol, x0, x1
