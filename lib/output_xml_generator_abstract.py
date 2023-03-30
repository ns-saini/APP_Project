"""Abstract class for generating an XML output file."""
import abc

class XMLHandler(abc.ABC):
    """
    Abstract base class for XML handler.
    """

    def __init__(self):
        
        super().__init__()

    @abc.abstractmethod
    def process_data(self):
        """
        Abstract method that generates an XML output file.
        """
    
