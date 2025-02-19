import xml.etree.ElementTree as ET

tree = ET.parse("employee.xml")
root = tree.getroot()
emp = ET.Element("employee")
empId = ET.Element("id")
empId.text='6'
emp.append(empId)
empName = ET.Element("name")
empName.text="Hồ Quang Vinh"
emp.append(empName)
root.append(emp)
tree.write('employee.xml', encoding='utf-8')