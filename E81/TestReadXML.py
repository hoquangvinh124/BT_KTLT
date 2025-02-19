import xml.etree.ElementTree as ET
from E81.employee import Employee

tree = ET.parse("employee.xml")
root = tree.getroot()
for child in root.findall("employee"):
    id = child.find("id").text
    name = child.find("name").text
    emp = Employee(int(id), name)
    print(emp)