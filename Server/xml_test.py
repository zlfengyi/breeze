import xml.etree.ElementTree as ET

tree = ET.parse('asr/bin/wav/2.xml')
root = tree.getroot()

print(root.tag)
for x in root.iter('trigger'):
    print(x.attrib, x.text)
