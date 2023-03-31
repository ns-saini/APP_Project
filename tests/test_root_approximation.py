'''Test the root approximation method.'''
import unittest
from lib.root_approximation import RootApproximationBI  as RABI
from lib.root_approximation import RootApproximationWBI as RAWBI

class TestRootApproximation(unittest.TestCase):
    '''Test the root approximation method.'''

    @staticmethod
    def test_root_approximation_bi():
        """Test the root approximation method with BI."""
        root_approx = RABI()
        assert[abs(round(root_approx.get_roots(lambda x: x**2 - 2, 0.0001)[0], 4))] == [1.4142]

    @staticmethod
    def test_root_approximation_wbi():
        """Test the root approximation method with WBI."""
        root_approx = RAWBI()
        assert [abs(round(root_approx.get_roots(lambda x: x**2 - 2, 0.0001)[0], 4))] == [1.4142]
