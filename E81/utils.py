import xml.etree.ElementTree as ET

def remove_employee(file, id_search):
    tree = ET.parse(file)
    root = tree.getroot()
    itemDelete = None
    for item in root.findall('employee'):
         id = int(item.find('id').text)
         if id == int(id_search):
            itemDelete = item
            break
    if itemDelete is not None:
        root.remove(itemDelete)
        tree.write(file, encoding='utf-8')

def edit_employee(file, id_search, new_name):
    tree = ET.parse(file)
    root = tree.getroot()
    for item in root.findall('employee'):
     id = item.find('id').text
     if int(id) == int(id_search):
         name = item.find('name')
         name.text = new_name
    tree.write(file, encoding='utf-8')

def insert_employee(file, id, name):
    tree = ET.parse(file)
    root = tree.getroot()
    emp = ET.Element("employee")
    empId = ET.Element("id")
    empId.text= id
    emp.append(empId)
    empName = ET.Element("name")
    empName.text = name
    emp.append(empName)
    root.append(emp)
    tree.write(file, encoding='utf-8')

def read_employee(file):
    list_employee = []
    from E81.employee import Employee
    tree = ET.parse(file)
    root = tree.getroot()
    for child in root.findall("employee"):
        id = child.find("id").text
        name = child.find("name").text
        emp = Employee(int(id), name)
        list_employee.append(emp)
    return list_employee

def find_to_edit_or_insert(file, id_search, search_name):
    existed = False
    tree = ET.parse(file)
    root = tree.getroot()
    for item in root.findall('employee'):
     id = item.find('id').text
     if int(id) == int(id_search):
         name = item.find('name')
         name.text = search_name
         existed = True
    if existed:
        edit_employee(file, id_search, search_name)
    else:
        insert_employee(file, id_search, search_name)

def search_id(file, id_search):
    list_employee = []
    from E81.employee import Employee
    tree = ET.parse(file)
    root = tree.getroot()
    for item in root.findall('employee'):
        id = item.find('id').text
        if int(id) == int(id_search):
            name = item.find('name').text
            emp = Employee(int(id), name.strip())
            list_employee.append(emp)
    return list_employee