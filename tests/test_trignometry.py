'''Test the trignometry class.'''''
import unittest
from lib.trignometry import Trignometry  as T
from lib.trignometry import TrignometryBI as TBI

class TestTrignometry(unittest.TestCase):
    '''Test the trignometry class.'''
    @staticmethod
    def test_sin():
        """Test the sin method."""
        trig = T()
        assert trig.sin(0) == 0

    @staticmethod
    def test_cos():
        """Test the cos method."""
        trig = T()
        assert trig.cos(0) == 1

    @staticmethod
    def test_sin_without_builtin():
        """Test the sin method without using built-in functions."""
        trig = TBI(2)
        assert round(trig.sin(0)) == 0

    @staticmethod
    def test_cos_without_builtin():
        """Test the cos method without using built-in functions."""
        trig = TBI(2)
        assert round(trig.cos(0)) == 1
