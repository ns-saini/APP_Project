import unittest
from lib.math_lib import MathLibBI as ML
from lib.math_lib import MathLibWBI as MLWBI
import math
class TestMathLib(unittest.TestCase):
    def test_pow(self):
        """Test the pow method."""
        m_lib = ML()
        assert m_lib.pow(2, 3) == 8

    def test_pow_without_builtin(self):
        """Test the pow method without using built-in functions."""
        m_lib = MLWBI()
        assert m_lib.pow(2, 3) == 8

    def test_pow_zero(self):
        """Test the pow method with zero as the input."""
        m_lib = ML()
        assert m_lib.pow(0, 0) == 1
    
    def test_pow_zero_power(self):
        """Test the pow method with zero as the power."""
        m_lib = ML()
        assert m_lib.pow(2, 0) == 1
    
    def test_pow_zero_number(self):
        """Test the pow method with zero as the number."""
        m_lib = ML()
        assert m_lib.pow(0, 2) == 0
    
    def test_pow_negative_power(self):
        """Test the pow method with a negative power."""
        m_lib = ML()
        assert m_lib.pow(2, -2) == 0.25
    
    def test_pow_negative_number(self):
        """Test the pow method with a negative number."""
        m_lib = ML()
        assert m_lib.pow(-2, 2) == 4
    
    def test_pow_negative_number_and_power(self):
        """Test the pow method with a negative number and power."""
        m_lib = ML()
        assert m_lib.pow(-2, -2) == 0.25
    
    def test_pow_zero_without_builtin(self):
        """Test the pow method with zero as the input without using built-in functions."""
        m_lib = MLWBI()
        assert m_lib.pow(0, 0) == 1

    def test_pow_zero_power_without_builtin(self):
        """Test the pow method with zero as the power without using built-in functions."""
        m_lib = MLWBI()
        assert m_lib.pow(2, 0) == 1

    def test_pow_zero_number_without_builtin(self):
        """Test the pow method with zero as the number without using built-in functions."""
        m_lib = MLWBI()
        assert m_lib.pow(0, 2) == 0

    def test_pow_negative_power_without_builtin(self):
        """Test the pow method with a negative power without using built-in functions."""
        m_lib = MLWBI()
        assert m_lib.pow(2, -2) == 0.25

    def test_pow_negative_number_without_builtin(self): 
        """Test the pow method with a negative number without using built-in functions."""
        m_lib = MLWBI()
        assert m_lib.pow(-2, 2) == 4

    def test_pow_negative_number_and_power_without_builtin(self):
        """Test the pow method with a negative number and power without using built-in functions."""
        m_lib = MLWBI()
        assert m_lib.pow(-2, -2) == 0.25

    def test_pi(self):
        """Test the pi method."""
        m_lib = ML()
        assert m_lib.get_pi() == 3.141592653589793

    def test_pi_without_builtin(self):
        """Test the pi method without using built-in functions. The approximation is accurate to 3 decimal places. """
        m_lib = MLWBI()
        assert abs(math.pi - m_lib.get_pi()) < 0.001

    def test_factorial(self):
        """Test the factorial method."""
        m_lib = ML()
        assert m_lib.factorial(3) == 6

    def test_factorial_without_builtin(self):
        """Test the factorial method without using built-in functions."""
        m_lib = MLWBI()
        assert m_lib.factorial(3) == 6

    def test_factorial_zero(self):
        """Test the factorial method with zero as the input."""
        m_lib = ML()
        assert m_lib.factorial(0) == 1
    
    def test_factorial_zero_without_builtin(self):
        """Test the factorial method with zero as the input without using built-in functions."""
        m_lib = MLWBI()
        assert m_lib.factorial(0) == 1
    
    def test_factorial_negative(self):
        """Test the factorial method with a negative number as the input."""
        m_lib = MLWBI()
        self.assertRaises(ValueError, m_lib.factorial, -1)


if __name__ == '__main__':
    unittest.main()