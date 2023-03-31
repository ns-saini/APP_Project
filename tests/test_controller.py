import math
import unittest
import pytest
from controller import Controller

class TestController(unittest.TestCase):

    def test_negative_radius(self):
        with pytest.raises(ValueError):
            controller = Controller(radius=-1)


    def test_zero_radius(self):
        with pytest.raises(ValueError):
            controller = Controller(radius=0)   


    # Test case for valid radius input
    def test_valid_radius(self):
        radius = 5
        controller = Controller(radius)
        assert controller.radius == radius


    def test_calculate_length_wbi(self):
        radius = 5
        controller = Controller(radius)
        expected_length = 6.579551664194772
        assert controller.calculate_length_wbi(radius) == expected_length


    def test_calculate_length_bi(self):
        radius = 1
        controller = Controller(radius)
        expected_length = 1.3163801959113433
        assert controller.calculate_length_bi(radius) == expected_length