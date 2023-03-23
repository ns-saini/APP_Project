'''
    XML generator
'''
import xml.etree.ElementTree as ET
from controller import Controller

class XMLHandler:
    '''
        XML Handler
    '''
    def __init__(self, input_ctrl, output_file):
        self.input_ctrl = input_ctrl
        self.output_file = output_file
    def process_data(self):
        """
        Generates an XML output file containing radius and corresponding length of a coaster track.

        Args:
        - output_file: the name of the output file to be created

        Returns:
        - None
        """
        # Create an instance of the Coaster class
        # I can just read the inputs from a function in controller

        # Create the root element of the XML output tree
        output_root = ET.Element("root")

        # Loop through the radius values to process
        for radius in self.input_ctrl:
        # Create an "element" element and add it to the output tree
        element_elem = ET.SubElement(output_root, "element")

        # Create a "radius" element and add it to the "element" element
        radius_elem = ET.SubElement(element_elem, "radius")
        radius_elem.text = str(radius)


        # Create an "output" element and add it to the "element" element
        output_elem = ET.SubElement(element_elem, "output")
        output_elem.text = str(length)

        # Create the ElementTree object and write it to a file
        output_tree = ET.ElementTree(output_root)
        output_tree.write(self.output_file, xml_declaration=True,
        #                   encoding="utf-8", method="xml", doctype=DTD)
        print(self.output_file)

    def temp_method(self):
        '''
            ...
        '''
        print('This is a temporary method')


DTD = '''<!DOCTYPE root [
    <!ELEMENT root (element*)>
    <!ELEMENT element (radius, output)>
    <!ELEMENT radius (#PCDATA)>
    <!ELEMENT output (#PCDATA)>
]>'''


