from JsonFactory import *
from ClassInfo import *

def load_categories():
    result = JsonFileFactory.read_data("Categories.json", Category)
    return result

def load_products():
    result = JsonFileFactory.read_data("Products.json", Product)
    return result