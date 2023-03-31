# from lib.output_xml_generator import MyXMLHandler
# import unittest
# import os
# from xml.dom import minidom
# import xml.etree.ElementTree as ET

# class TestXMLHandler(unittest.TestCase):
#     def test_process_data(self):
#         # Set up test input and output
#         input_ctrl = 5.0
#         output_file = 'output.xml'

#         # Create an instance of the MyXMLHandler class
#         xml_handler = MyXMLHandler(input_ctrl, output_file)

#         # Call the process_data method
#         xml_handler.process_data()

#         # Assert that the output file was created
#         self.assertTrue(os.path.exists(output_file))

#         # Assert that the output file is a valid XML file
#         try:
#             with open(output_file, 'r') as f:
#                 output_xml = f.read()
#             ElementTree = ET.ElementTree(ET.Element("root"))
#             ElementTree.parse(output_file)
#         except Exception as e:
#             self.fail("Output file is not a valid XML file: {}".format(str(e)))
#         # Assert that the output XML matches the expected XML
#         expected_xml = minidom.parseString('<root><element><radius>5.0</radius><output>6.579551664194772</output></element></root>').toprettyxml()
#         self.assertEqual(output_xml.strip(), expected_xml.strip())

#         # Clean up the output file
#         os.remove(output_file)


#====================================================================================
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

