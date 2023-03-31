import math
import unittest
import pytest
from controller import Controller

class TestController(unittest.TestCase):

    def test_radius_positive(self):
        controller = Controller()
        # assert controller.calculate_length_bi(5) == 6.581900979556716
        self.assertAlmostEqual( controller.calculate_length_wbi(2),  2.6318206)