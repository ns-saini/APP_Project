from lib import root_approximation as ra
from lib import trignometry as t
from lib import math_lib as ml


if __name__ == '__main__':
    a = ra.RootApproximation_WBI()
    mathLib = ml.MathLib_BI()
    mathLib2 = ml.MathLib_WBI()
    tbi = t.TrignometryBI(precision=4)
    twbi = t.TrignometryWBI(precision=4)

    # print(mathLib2.pow(2,-2))

    # print(mathLib.get_pi())
    # print(mathLib2.get_pi())

    print("cos_bi", tbi.cos(1))
    print("cos_wbi",twbi.cos(1))

    print("sin_bi", tbi.sin(1))
    print("sin_wbi", twbi.sin(1))


    b = ra.RootApproximation_BI()
    
    f_bi = lambda x: x ** 2 + tbi.sin(x) - 2
    f_wbi = lambda x: x ** 2 + twbi.sin(x) - 2

    roots_bi = b.get_roots(f_bi, 0.0001)
    roots_wbi = a.get_roots(f_wbi, .0001)

    l_bi = 2*1*(1-tbi.cos(roots_bi[0]/2))
    l_wbi = 2*1*(1-twbi.cos(float(roots_wbi[0]/2)))
    print(l_bi, l_wbi)
    