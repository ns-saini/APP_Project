from lib import controller as ctrl
import xml.etree.ElementTree as ET

out = ctrl.lenght_calculator()

root = ET.Element('result')
root.text = 'Lenght' + ' = ' + str(out)
ET.dump(root)
