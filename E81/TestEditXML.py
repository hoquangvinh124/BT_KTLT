import xml.etree.ElementTree as ET

tree = ET.parse("employee.xml")
root = tree.getroot()
idSearch = 4
newName = "Cô Ba Vàng Ngọc"
for item in root.findall('employee'):
 id = item.find('id').text
 if int(id) == idSearch:
     name = item.find('name')
     name.text=newName
tree.write('employee.xml', encoding='utf-8')