import unittest
from lib.trignometry import Trignometry  as T
from lib.trignometry import TrignometryBI as TBI

class TestTrignometry(unittest.TestCase):
    def test_sin(self):
        """Test the sin method."""
        trig = T()
        assert trig.sin(0) == 0
    
    def test_cos(self):
        """Test the cos method."""
        trig = T()
        assert trig.cos(0) == 1
    
    def test_sin_without_builtin(self):
        """Test the sin method without using built-in functions."""
        trig = TBI(2)
        assert round(trig.sin(0)) == 0
    
    def test_cos_without_builtin(self):
        """Test the cos method without using built-in functions."""
        trig = TBI(2)
        assert round(trig.cos(0)) == 1