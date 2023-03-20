from lib import root_approximation as ra
from lib import trignometry as t
from lib import math_lib as ml
from lib import input_validator


def main():
    a = ra.RootApproximation()
    math_lib = ml.MathLib()
    m = t.Trignometry(m_lib=math_lib)
    tol, x0, x1 = input_validator.validate_input()
    f = lambda x: x ** 2 + m.sin(x) - 2
    root = a.secant_approximation(f, x0, x1, tol)
    print(f"The root of the function is approximately: {root:.4f}")


if __name__ == '__main__':
    main()