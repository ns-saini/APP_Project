'''
main module
'''
import controller as ct
from lib import input_validator
from lib import output_xml_generator

def main():
    '''
    main method
    '''

    radius = float(input_validator.validate_input())
    controller = ct.Controller(radius)
    length = controller.calculate_length_wbi(radius)
    xml_handler = output_xml_generator.MyXMLHandler(radius, length)
    xml_handler.process_data()
    controller.calculate_length_bi(radius)


if __name__ == '__main__':
    main()
