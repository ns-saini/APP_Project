from lib import root_approximation as ra
from lib import trignometry as t
from lib import math_lib as ml
if __name__ == '__main__':
    a = ra.RootApproximation()
    mathLib = ml.MathLib()
    m = t.Trignometry(m_lib=mathLib)

    f = lambda x: x ** 2 + m.sin(x) - 2
    print(a.secant_approximation(f, 0, 1, .0001))
