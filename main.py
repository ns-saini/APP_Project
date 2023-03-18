from lib import root_approximation as ra
from lib import trignometry as t
from lib import math_lib as ml
import math


if __name__ == '__main__':
    a = ra.RootApproximation_WBI()
    mathLib = ml.MathLib_BI()
    mathLib2 = ml.MathLib_WBI()
    tbi = t.TrignometryBI(precision=4)
    twbi = t.TrignometryWBI(precision=4)

    # print(mathLib2.pow(2,-2))

    # print(mathLib.get_pi())
    # print(mathLib2.get_pi())

    print(tbi.cos(mathLib.get_pi()))
    print(twbi.cos(mathLib.get_pi()))

    print(tbi.sin(mathLib.get_pi()))
    print(twbi.sin(mathLib.get_pi()))


    b = ra.RootApproximation_BI()

    f = lambda x: x ** 2 + tbi.sin(x) - 2
    
    r = b.get_roots(f, 0.0001)
    a.get_roots(f, .0001)

    l = 2*1*(1-twbi.cos(r[0]/2))
    print(l)
    