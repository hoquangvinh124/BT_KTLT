import xml.etree.ElementTree as ET
from E93.TestXML.product_class import Product

class XMLFunction:
    @staticmethod
    def read_xml(file):
        list_of_product = []
        tree = ET.parse(file)
        root = tree.getroot()
        for item in root.findall("product"):
            id = item.get("id")
            name = item.find("name").text
            price = item.find("price").text
            file_path_element = item.find("file_path")
            file_path = file_path_element.text if file_path_element is not None else "../Images/tiger.png"
            p = Product(int(id), name, float(price), file_path)
            list_of_product.append(p)
        return list_of_product
    @staticmethod
    def write_xml(file, new_id, new_name, new_price):
        tree = ET.parse(file)
        root = tree.getroot()
        product_tag = ET.SubElement(root, "product", id=new_id)
        name = ET.SubElement(product_tag, "name")
        name.text = new_name
        price = ET.SubElement(product_tag, "price")
        price.text = str(new_price)
        tree.write(file, encoding='utf-8')
    @staticmethod
    def remove_xml(file, search_id):
        tree = ET.parse(file)
        root = tree.getroot()
        itemDelete = None
        for item in root.findall('product'):
            id = int(item.get("id"))
            if id == int(search_id):
                itemDelete = item
                break
        if itemDelete is not None:
            root.remove(itemDelete)
            tree.write(file, encoding='utf-8')
    @staticmethod
    def edit_xml(file, search_id, new_name, new_price):
        tree = ET.parse(file)
        root = tree.getroot()
        for item in root.findall('product'):
            id = item.get("id")
            if int(id) == int(search_id):
                name = item.find('name')
                name.text = new_name
                price = item.find('price')
                price.text = new_price
        tree.write(file, encoding='utf-8')
    @staticmethod
    def find_to_edit_or_insert(file, id_search, search_name, new_price):
        existed = False
        tree = ET.parse(file)
        root = tree.getroot()
        for item in root.findall('product'):
            id = item.get("id")
            if int(id) == int(id_search):
                name = item.find('name')
                name.text = search_name
                existed = True
        if existed:
            XMLFunction.edit_xml(file, id_search, search_name, new_price)
        else:
            XMLFunction.write_xml(file, id_search, search_name, new_price)
    @staticmethod
    def sort_products(products):
        for i in range(len(products)):
            for j in range(len(products)):
                pi = products[i]
                pj = products[j]
                if pi.price < pj.price:
                    products[i] = pj
                    products[j] = pi
        return products
    @staticmethod
    def sort_products_desc(products):
        n = len(products)
        for i in range(n - 1):
            max_idx = i
            for j in range(i + 1, n):
                if products[j].price > products[max_idx].price:
                    max_idx = j
            if max_idx != i:
                products[i], products[max_idx] = products[max_idx], products[i]
        return products
