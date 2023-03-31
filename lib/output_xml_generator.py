'''
    XML generator
'''
import xml.etree.ElementTree as ET
from lib.output_xml_generator_abstract import XMLHandler


class MyXMLHandler(XMLHandler):
    """
    Concrete implementation of XML handler.
    """

    def __init__(self, input_ctrl, output_file):
        self.input_ctrl = input_ctrl
        self.output_file = output_file
        super().__init__()

    def process_data(self):
        # Create the root element of the XML output tree
        output_root = ET.Element("root")
        # output_root.insert(0, ET.fromstring(DTD))

        # Loop through the radius values to process
        # Create an "element" element and add it to the output tree
        element_elem = ET.SubElement(output_root, "element")

        # Create a "radius" element and add it to the "element" element
        radius_elem = ET.SubElement(element_elem, "radius")
        radius_elem.text = str(self.input_ctrl)

        # Create an "output" element and add it to the "element" element
        output_elem = ET.SubElement(element_elem, "output")
        output_elem.text = str(self.output_file)

        # Create the ElementTree object and write it to a file
        output_tree = ET.ElementTree(output_root)
        output_tree.write('output.xml', xml_declaration=True,
                          encoding="utf-8", method="xml")

        return self.output_file

    def temp_method(self):
        """
        Temporary method.
        """
        