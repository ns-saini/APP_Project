'''write multiple test cases for the input validator function using unittest'''

import unittest
from unittest.mock import patch
from lib.input_validator import validate_input

class TestInputValidator(unittest.TestCase):

    '''Test the input validator function'''
    @patch('builtins.input', side_effect=['0.0001'])
    def test_validate_input(self, mock_input):
        self.assertEqual(validate_input(), 0.0001)

    '''Test the input validator function with negative input'''

    @patch('builtins.input', side_effect=['-1'])
    def test_validate_input_negative(self, mock_input):
        self.assertEqual(ValueError, validate_input)

    '''Test the input validator function with non-numeric input'''

    @patch('builtins.input', side_effect=['a'])
    def test_validate_input_non_numeric(self, mock_input):
        self.assertEqual(ValueError, validate_input)

    '''Test the input validator function with zero input'''
    @patch('builtins.input', side_effect=['0'])
    def test_validate_input_zero(self, mock_input):
        self.assertEqual(ValueError, validate_input)
    
    '''Test the input validator function with empty input'''
    @patch('builtins.input', side_effect=[''])
    def test_validate_input_empty(self, mock_input):
        self.assertEqual(ValueError, validate_input)
    
    '''Test the input validator function with one input'''
    @patch('builtins.input', side_effect=['1'])
    def test_validate_input_one(self, mock_input):
        self.assertEqual(validate_input(), 1)
    
    '''Test the input validator function with space inputs'''
    @patch('builtins.input', side_effect=[' '])
    def test_validate_input_space(self, mock_input):
        self.assertEqual(ValueError, validate_input)
    
    '''special characters'''
    @patch('builtins.input', side_effect=['!'])
    def test_validate_input_special_characters(self, mock_input):
        self.assertEqual(ValueError, validate_input)
    
    '''big integer'''
    @patch('builtins.input', side_effect=['100000'])
    def test_validate_input_big_integer(self, mock_input):
        self.assertEqual(validate_input(), 100000)

    '''big float'''
    @patch('builtins.input', side_effect=['100000.0001'])
    def test_validate_input_big_float(self, mock_input):
        self.assertEqual(validate_input(), 100000.0001)
    
    '''big float with negative'''
    @patch('builtins.input', side_effect=['-100000.0001'])
    def test_validate_input_big_float_negative(self, mock_input):
        self.assertEqual(ValueError, validate_input)
    
    '''big integer with negative'''
    @patch('builtins.input', side_effect=['-100000'])
    def test_validate_input_big_integer_negative(self, mock_input):
        self.assertEqual(ValueError, validate_input)

    '''big float with space'''
    @patch('builtins.input', side_effect=[' 100000.0001'])
    def test_validate_input_big_float_space(self, mock_input):
        self.assertEqual(ValueError, validate_input)
    
    '''big integer with space'''
    @patch('builtins.input', side_effect=[' 100000'])
    def test_validate_input_big_integer_space(self, mock_input):
        self.assertEqual(ValueError, validate_input)
    
    '''big float with special characters'''
    @patch('builtins.input', side_effect=['!100000.0001'])
    def test_validate_input_big_float_special_characters(self, mock_input):
        self.assertEqual(ValueError, validate_input)
    
    '''big integer with special characters'''
    @patch('builtins.input', side_effect=['!100000'])
    def test_validate_input_big_integer_special_characters(self, mock_input):
        self.assertEqual(ValueError, validate_input)
    
    '''big float with negative and space'''
    @patch('builtins.input', side_effect=[' -100000.0001'])
    def test_validate_input_big_float_negative_space(self, mock_input):
        self.assertEqual(ValueError, validate_input)
    

if __name__ == '__main__':
    unittest.main()