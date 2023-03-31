''' Tests for the controller module.'''
import unittest
from controller import Controller

class TestController(unittest.TestCase):
    '''Tests for the Controller class.'''

    def test_radius_positive(self):
        """Test the calculate_length_wbi method with a positive radius without builtin functions."""
        controller = Controller()
        self.assertEqual( round(controller.calculate_length_wbi(2),2),  2.63)

    def test_radius_zero(self):
        '''Test the calculate_length_wbi method with a zero radius without builtin functions.'''
        controller = Controller()
        self.assertEqual( round(controller.calculate_length_wbi(0),2),  0)

    def test_radius_negative(self):
        """Test the calculate_length_wbi method with a negative radius without builtin functions."""
        controller = Controller()
        self.assertEqual( round(controller.calculate_length_wbi(-2),2),  -2.63)

    def test_radius_positive_builtin(self):
        """Test the calculate_length_wbi method with a positive radius with builtin functions."""
        controller = Controller()
        self.assertEqual( round(controller.calculate_length_bi(2),2),  2.63)

    def test_radius_zero_builtin(self):
        '''Test the calculate_length_wbi method with a zero radius with builtin functions.'''
        controller = Controller()
        self.assertEqual( round(controller.calculate_length_bi(0),2),  0)

    def test_radius_negative_builtin(self):
        """Test the calculate_length_wbi method with a negative radius with builtin functions."""
        controller = Controller()
        self.assertEqual( round(controller.calculate_length_bi(-2),2),  -2.63)
