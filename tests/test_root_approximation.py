import unittest
from lib.root_approximation import RootApproximationBI  as RABI
from lib.root_approximation import RootApproximationWBI as RAWBI
import math

class TestRootApproximation(unittest.TestCase):
    def test_root_approximation_bi(self):
        """Test the root approximation method with BI."""
        root_approx = RABI()

        assert[abs(round(root_approx.get_roots(lambda x: x**2 - 2, 0.0001)[0], 4))] == [1.4142]

    def test_root_approximation_wbi(self):
        """Test the root approximation method with WBI."""
        root_approx = RAWBI()

        print(root_approx.get_roots(lambda x: x**2 - 2, 0.0001))
        assert [abs(round(root_approx.get_roots(lambda x: x**2 - 2, 0.0001)[0], 4))] == [1.4142]

