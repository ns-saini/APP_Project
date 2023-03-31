import unittest
import os
from lib.output_xml_generator import MyXMLHandler

class TestMyXMLHandler(unittest.TestCase):
    def setUp(self):
        self.input_ctrl = 5.0
        self.output_file = "output.xml"
        self.handler = MyXMLHandler(self.input_ctrl, self.output_file)

    def tearDown(self):
        if os.path.exists(self.output_file):
            os.remove(self.output_file)

    def test_process_data(self):
        output = self.handler.process_data()
        self.assertEqual(output, self.output_file)
        self.assertTrue(os.path.exists(self.output_file))
        with open(self.output_file, 'r') as f:
            contents = f.read()
            self.assertIn("<root>", contents)
            self.assertIn("<element>", contents)
            self.assertIn("<radius>5.0</radius>", contents)
            self.assertIn("<output>output.xml</output>", contents)
            self.assertIn("</element>", contents)
            self.assertIn("</root>", contents)
#====================================================================================


# class TestMyXMLHandler(unittest.TestCase):
#     def setUp(self):
#         self.input_ctrl = 5.0
#         self.output_file = "output.xml"
#         self.handler = MyXMLHandler(self.input_ctrl, self.output_file)

#     def tearDown(self):
#         if os.path.exists(self.output_file):
#             os.remove(self.output_file)

#     def test_process_data(self):
#         output = self.handler.process_data()
#         self.assertEqual(output, self.output_file)
#         self.assertTrue(os.path.exists(self.output_file))
#         with open(self.output_file, 'r') as f:
#             contents = f.read()
#             self.assertIn("<root>", contents)
#             self.assertIn("<element>", contents)
#             self.assertIn("<radius>5.0</radius>", contents)
#             self.assertIn("<output>output.xml</output>", contents)
#             self.assertIn("</element>", contents)
#             self.assertIn("</root>", contents)

