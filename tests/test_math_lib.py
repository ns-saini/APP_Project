import unittest
from lib.math_lib import MathLibBI as ML
from lib.math_lib import MathLibWBI as MLWBI

class TestMathLib(unittest.TestCase):
    def test_pow(self):
        """Test the pow method."""
        m_lib = ML()
        assert m_lib.pow(2, 3) == 8

    def test_pow_without_builtin(self):
        """Test the pow method."""
        m_lib = MLWBI()
        assert m_lib.pow(2, 3) == 8


if __name__ == '__main__':
    unittest.main()