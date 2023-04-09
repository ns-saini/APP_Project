''' Test the input validator function '''
import unittest
from unittest.mock import patch
from lib.input_validator import validate_input


class TestInputValidator(unittest.TestCase):
    '''Test the input validator function'''

    @patch('builtins.input', side_effect=['0.0001'])
    def test_validate_input(self, mock_input):
        '''Test the input validator function'''
        print(mock_input)
        self.assertEqual(validate_input(), 0.0001)

    @patch('builtins.input', side_effect=['-1'])
    def test_validate_input_negative(self, mock_input):
        '''Test the input validator function with negative input '''
        print(mock_input)
        self.assertRaises(Exception, validate_input)

    @patch('builtins.input', side_effect=['a'])
    def test_validate_input_non_numeric(self, mock_input):
        '''Test the input validator function with non-numeric input'''
        print(mock_input)
        self.assertRaises(Exception, validate_input)

    @patch('builtins.input', side_effect=['0'])
    def test_validate_input_zero(self, mock_input):
        '''Test the input validator function with zero input'''
        print(mock_input)
        self.assertRaises(Exception, validate_input)

    @patch('builtins.input', side_effect=[''])
    def test_validate_input_empty(self, mock_input):
        '''Test the input validator function with empty input'''
        print(mock_input)
        self.assertRaises(Exception, validate_input)

    @patch('builtins.input', side_effect=['1'])
    def test_validate_input_one(self, mock_input):
        '''Test the input validator function with one input'''
        print(mock_input)
        self.assertEqual(validate_input(), 1)

    @patch('builtins.input', side_effect=[' '])
    def test_validate_input_space(self, mock_input):
        '''Test the input validator function with space inputs'''
        print(mock_input)
        self.assertRaises(Exception, validate_input)

    @patch('builtins.input', side_effect=['!'])
    def test_validate_input_special_characters(self, mock_input):
        '''special characters'''
        print(mock_input)
        self.assertRaises(Exception, validate_input)

    @patch('builtins.input', side_effect=['100000'])
    def test_validate_input_big_integer(self, mock_input):
        '''big integer'''
        print(mock_input)
        self.assertEqual(validate_input(), 100000)

    @patch('builtins.input', side_effect=['100000.0001'])
    def test_validate_input_big_float(self, mock_input):
        '''big float'''
        print(mock_input)
        self.assertEqual(validate_input(), 100000.0001)

    @patch('builtins.input', side_effect=['-100000.0001'])
    def test_validate_input_big_float_negative(self, mock_input):
        '''big float with negative'''
        print(mock_input)
        self.assertRaises(Exception, validate_input)

    @patch('builtins.input', side_effect=['-100000'])
    def test_validate_input_big_integer_negative(self, mock_input):
        '''big integer with negative'''
        print(mock_input)
        self.assertRaises(Exception, validate_input)

    @patch('builtins.input', side_effect=[' 100000.0001'])
    def test_validate_input_big_float_space(self, mock_input):
        '''big float with space'''
        print(mock_input)
        self.assertEqual(validate_input(), 100000.0001)

    @patch('builtins.input', side_effect=[' 100000'])
    def test_validate_input_big_integer_space(self, mock_input):
        '''big integer with space'''
        print(mock_input)
        self.assertEqual(validate_input(), 100000)

    @patch('builtins.input', side_effect=['!100000.0001'])
    def test_validate_input_big_float_special_characters(self, mock_input):
        '''big float with special characters'''
        print(mock_input)
        self.assertRaises(Exception, validate_input)

    @patch('builtins.input', side_effect=['!100000'])
    def test_validate_input_big_integer_special_characters(self, mock_input):
        '''big integer with special characters'''
        print(mock_input)
        self.assertRaises(Exception, validate_input)

    @patch('builtins.input', side_effect=[' -100000.0001'])
    def test_validate_input_big_float_negative_space(self, mock_input):
        '''big float with negative and space'''
        print(mock_input)
        self.assertRaises(Exception, validate_input)

    @patch('builtins.input', side_effect=['3.1415'])
    def test_validate_input_decimal(self, mock_input):
        '''Test the input validator function with a decimal input'''
        print(mock_input)
        self.assertEqual(validate_input(), 3.1415)

    @patch('builtins.input', side_effect=['123456789'])
    def test_validate_input_large_integer(self, mock_input):
        '''Test the input validator function with a large integer input'''
        print(mock_input)
        self.assertEqual(validate_input(), 123456789)

    @patch('builtins.input', side_effect=['-123456789'])
    def test_validate_input_large_negative_integer(self, mock_input):
        '''Test the input validator function with a large negative integer input'''
        print(mock_input)
        self.assertRaises(Exception, validate_input)

if __name__ == '__main__':
    unittest.main()
