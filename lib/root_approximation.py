class RootApproximation:
    def __init__(self):
        """
        Initializes an instance of the RootApproximation class with a default value of 100 for the number of terms.
        """
        self.num_terms = 100

    def secant_approximation(self, func, x0, x1, e):
        """
        Uses the secant method to approximate the root of a given function within a given tolerance.

        Args:
        - func: the function to be approximated
        - x0: the initial guess for the root
        - x1: the second initial guess for the root
        - e: the tolerance for the approximation

        Returns:
        - The approximation for the root of the given function within the given tolerance.
        """

        x2 = 0
        step = 1
        while True:
            if func(x0) == func(x1):
                break

            x2 = x0 - (x1 - x0) * func(x0) / (func(x1) - func(x0))
            print('Iteration-%d, x2 = %0.6f and f(x2) = %0.6f' % (step, x2, func(x2)))

            x0 = x1
            x1 = x2
            step += 1

            if step > self.num_terms:
                print("Not convergent")
                break

            if func(x2) - func(x1) > e:
                break

        return x2
