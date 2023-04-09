"""Scipy root approximation module."""
from scipy.optimize import fsolve

from lib.root_approximation_abstract import RootApproximation


class RootApproximationWBI(RootApproximation):
    """RootApproximation_WBI class for calculating the root of a
      function using the secant method."""

    def __init__(self):
        """
        Initializes an instance of the RootApproximation class with a
          default value of 100 for the number of terms.
        """
        self.num_terms = 100
        super().__init__()

    def get_roots(self, func, error) -> list:
        """
        Uses the secant method to approximate the root of a given function
        within a given tolerance.

        Args:
        - func: the function to be approximated
        - x0: the initial guess for the root
        - x1: the second initial guess for the root
        - e: the tolerance for the approximation

        Returns:
        - The approximation for the root of the given function within the given tolerance.
        """
        x_0 = -1000.01
        x_1 = +1000
        x_2 = 0
        step = 1
        while True:
            if func(x_0) == func(x_1):
                break

            x_2 = x_0 - (x_1 - x_0) * func(x_0) / (func(x_1) - func(x_0))
            # print(
                # f'Iteration-{step}, x2 = {x_2:.6f} and f(x2) = {func(x_2):.6f}')

            x_0 = x_1
            x_1 = x_2
            step += 1

            if step > self.num_terms:
                raise RuntimeError("Not convergent")

            if func(x_2) - func(x_1) > error:
                break

        return [x_2]

    def temp_method(self):
        '''
            ...
        '''
        print('This is a temporary method')



class RootApproximationBI(RootApproximation):
    """RootApproximation_BI class for calculating the root of a
      function using the `fsolve` method."""

    def __init__(self) -> None:
        super().__init__()
        self.num_terms = 100

    def get_roots(self, func, error) -> list:
        """
        Calculates the root of a given function using the `fsolve` method.

        Args:
            func (function): The function to calculate the root of.
            e (float): The precision of the root.

        Returns:
            list: The root of the function.
        """
        root = fsolve(func, 1)
        return root

    def temp_method(self):
        '''
            ...
        '''
        print('This is a temporary method')
