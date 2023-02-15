from lib import root_approximation as ra


if __name__ == '__main__':
    a = ra.RootApproximation()
    f = lambda x: x ** 2 - 2
    print(a.secant_approximation(f, 0, 1, .0001))
