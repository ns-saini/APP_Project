'''Test the math_lib module.'''
import unittest
import math
from lib.math_lib import MathLibBI as ML
from lib.math_lib import MathLibWBI as MLWBI

class TestMathLib(unittest.TestCase):
    '''Test the math_lib module.'''
    @staticmethod
    def test_pow():
        """Test the pow method."""
        m_lib = ML()
        assert m_lib.pow(2, 3) == 8

    @staticmethod
    def test_pow_without_builtin():
        """Test the pow method without using built-in functions."""
        m_lib = MLWBI()
        assert m_lib.pow(2, 3) == 8

    @staticmethod
    def test_pow_zero():
        """Test the pow method with zero as the input."""
        m_lib = ML()
        assert m_lib.pow(0, 0) == 1

    @staticmethod
    def test_pow_zero_power():
        """Test the pow method with zero as the power."""
        m_lib = ML()
        assert m_lib.pow(2, 0) == 1

    @staticmethod
    def test_pow_zero_number():
        """Test the pow method with zero as the number."""
        m_lib = ML()
        assert m_lib.pow(0, 2) == 0

    @staticmethod
    def test_pow_negative_power():
        """Test the pow method with a negative power."""
        m_lib = ML()
        assert m_lib.pow(2, -2) == 0.25

    @staticmethod
    def test_pow_negative_number():
        """Test the pow method with a negative number."""
        m_lib = ML()
        assert m_lib.pow(-2, 2) == 4

    @staticmethod
    def test_pow_negative_number_and_power():
        """Test the pow method with a negative number and power."""
        m_lib = ML()
        assert m_lib.pow(-2, -2) == 0.25

    @staticmethod
    def test_pow_zero_without_builtin():
        """Test the pow method with zero as the input without using built-in functions."""
        m_lib = MLWBI()
        assert m_lib.pow(0, 0) == 1

    @staticmethod
    def test_pow_zero_power_without_builtin():
        """Test the pow method with zero as the power without using built-in functions."""
        m_lib = MLWBI()
        assert m_lib.pow(2, 0) == 1

    @staticmethod
    def test_pow_zero_number_without_builtin():
        """Test the pow method with zero as the number without using built-in functions."""
        m_lib = MLWBI()
        assert m_lib.pow(0, 2) == 0

    @staticmethod
    def test_pow_negative_power_without_builtin():
        """Test the pow method with a negative power without using built-in functions."""
        m_lib = MLWBI()
        assert m_lib.pow(2, -2) == 0.25

    @staticmethod
    def test_pow_negative_number_without_builtin():
        """Test the pow method with a negative number without using built-in functions."""
        m_lib = MLWBI()
        assert m_lib.pow(-2, 2) == 4

    @staticmethod
    def test_pow_negative_number_and_power_without_builtin():
        """Test the pow method with a negative number and power without using built-in functions."""
        m_lib = MLWBI()
        assert m_lib.pow(-2, -2) == 0.25

    @staticmethod
    def test_pi():
        """Test the pi method."""
        m_lib = ML()
        assert m_lib.get_pi() == 3.141592653589793

    @staticmethod
    def test_pi_without_builtin():
        """Test the pi method without using built-in functions.
        The approximation is accurate to 3 decimal places. """
        m_lib = MLWBI()
        assert abs(math.pi - m_lib.get_pi()) < 0.001

    @staticmethod
    def test_factorial():
        """Test the factorial method."""
        m_lib = ML()
        assert m_lib.factorial(3) == 6

    @staticmethod
    def test_factorial_without_builtin():
        """Test the factorial method without using built-in functions."""
        m_lib = MLWBI()
        assert m_lib.factorial(3) == 6

    @staticmethod
    def test_factorial_zero():
        """Test the factorial method with zero as the input."""
        m_lib = ML()
        assert m_lib.factorial(0) == 1

    @staticmethod
    def test_factorial_zero_without_builtin():
        """Test the factorial method with zero as the input without using built-in functions."""
        m_lib = MLWBI()
        assert m_lib.factorial(0) == 1

if __name__ == '__main__':
    unittest.main()
