def calculate_pi():
    val = 0.0
    total_terms = 100
    for i in range(1, 2 * total_terms, 2):
        sign = -(i % 4 - 2)
        val += float(sign) / i
    return 4 * val


class MathLib:
    def __init__(self):
        self.PI = None

    def exp(self, number, power):
        if power == 0:
            return 1
        temp = self.exp(number, int(power / 2))
        if power % 2 == 0:
            return temp * temp
        else:
            return temp * temp * temp

    def factorial(self, num):
        if num < 0:
            raise Exception("Factorial can't be calculated for negative numbers")
        result = 1
        for i in range(1, num + 1):
            result *= i
        return result

    def get_pi(self):
        if self.PI is not None:
            return self.PI
        return calculate_pi()

