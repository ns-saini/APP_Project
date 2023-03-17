from lib import root_approximation as ra
from lib import trignometry as t
from lib import math_lib as ml

if __name__ == '__main__':
    a = ra.RootApproximation_WBI()
    mathLib = ml.MathLib_BI(precision=0.0001)
    m = t.TrignometryBI(precision=4)

    b = ra.RootApproximation_BI()

    f = lambda x: x ** 2 + m.sin(x) - 2

    print(b.get_roots(f, 0.0001))

    print(a.get_roots(f, .0001))
