import math
import unittest
import pytest
from controller import Controller

class TestController(unittest.TestCase):

    """Test the negative value of radius."""
    def test_negative_radius(self):
        with pytest.raises(ValueError):
            controller = Controller(radius=-1)


    """Test for radius = 0"""
    def test_zero_radius(self):
        with pytest.raises(ValueError):
            controller = Controller(radius=0)   


    """Test case for valid radius input"""
    def test_valid_radius(self):
        radius = 5
        controller = Controller(radius)
        assert controller.radius == radius

    """Test case for integer value of radius"""
    def test_radius_not_character(self):
        with pytest.raises(TypeError):
            radius = 'a'
            controller = Controller(radius)
            controller.calculate_length()

    """Test case for  calculate length without using built in library method"""
    def test_calculate_length_wbi(self):
        radius = 5
        controller = Controller(radius)
        expected_length = 6.579551664194772
        assert controller.calculate_length_wbi(radius) == expected_length

    """Test case for  calculate length using built in library method"""
    def test_calculate_length_bi(self):
        radius = 1
        controller = Controller(radius)
        expected_length = 1.3163801959113433
        assert controller.calculate_length_bi(radius) == expected_length