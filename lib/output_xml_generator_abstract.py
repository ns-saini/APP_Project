"""Abstract class for generating an XML output file."""
import abc
import xml.etree.ElementTree as ET

class XMLHandler(abc.ABC):
    """
    Abstract base class for XML handler.
    """

    def __init__(self, input_ctrl, output_file):
        self.input_ctrl = input_ctrl
        self.output_file = output_file
        super().__init__()

    @abc.abstractmethod
    def process_data(self):
        """
        Abstract method that generates an XML output file.
        """

class MyXMLHandler(XMLHandler):
    """
    Concrete implementation of XML handler.
    """
