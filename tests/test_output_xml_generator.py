from lib.output_xml_generator import MyXMLHandler
import unittest
import os
from xml.dom import minidom
import xml.etree.ElementTree as ET

class TestXMLHandler(unittest.TestCase):
    def test_process_data(self):
        # Set up test input and output
        input_ctrl = 5.0
        output_file = 'test_output.xml'

        # Create an instance of the MyXMLHandler class
        xml_handler = MyXMLHandler(input_ctrl, output_file)

        # Call the process_data method
        xml_handler.process_data()

        # Assert that the output file was created
        self.assertTrue(os.path.exists(output_file))

        # Assert that the output file is a valid XML file
        try:
            with open(output_file, 'r') as f:
                output_xml = f.read()
            ElementTree = ET.ElementTree(ET.Element("root"))
            ElementTree.parse(output_file)
        except Exception as e:
            self.fail("Output file is not a valid XML file: {}".format(str(e)))
        # Assert that the output XML matches the expected XML
        expected_xml = minidom.parseString('<root><element><radius>5.0</radius><output>test_output.xml</output></element></root>').toprettyxml()
        self.assertEqual(output_xml.strip(), expected_xml.strip())

        # Clean up the output file
        os.remove(output_file)