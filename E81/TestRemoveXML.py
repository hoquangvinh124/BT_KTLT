import xml.etree.ElementTree as ET

tree = ET.parse("employees.xml")
root = tree.getroot()
idSearch = 4
itemDelete = None
for item in root.findall('employee'):
     id = int(item.find('id').text)
     if id ==idSearch:
        itemDelete=item
        break
if itemDelete is not None:
    root.remove(itemDelete)
    tree.write('employees.xml', encoding='utf-8')