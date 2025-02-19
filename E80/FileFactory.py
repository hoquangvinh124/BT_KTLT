import traceback

from E80.Product import Product

class FileFactory:
    @staticmethod
    def write_data(path, product):
        try:
            line = product.product_id + ";" + product.product_name + ";" + str(product.unit_price)
            with open(path, "a", encoding='utf-8') as file:
                file.writelines(line)
                file.writelines("\n")
            return True
        except:
            traceback.print_exc()
            return False
    @staticmethod
    def read_data(path):
        products = []
        try:
            with open(path, "r", encoding='utf-8') as file:
                for line in file:
                    data = line.strip()
                    arr = data.split(";")
                    product = Product(arr[0], arr[1], float(arr[2]))
                    products.append(product)
            return products
        except:
            traceback.print_exc()
            return []

    @staticmethod
    def edit_data(path, product_id, new_product):
        try:
            with open(path, "r", encoding="utf-8") as file:
                lines = file.readlines()

            updated = False
            with open(path, "w", encoding="utf-8") as file:
                for line in lines:
                    parts = line.strip().split(";")
                    if parts[0] == product_id:
                        line = new_product.product_id + ";" + new_product.product_name + ";" + str(
                            new_product.unit_price) + "\n"
                        updated = True
                    file.write(line)

            return updated

        except:
            traceback.print_exc()
            return False
    @staticmethod
    def check_product_exists(path, product_id):
        try:
            with open(path, "r", encoding="utf-8") as file:
                for line in file:
                    parts = line.strip().split(";")
                    if parts[0] == product_id:
                        return True
            return False
        except FileNotFoundError:
            print("File không tồn tại!")
            return False
        except Exception as e:
            print(f"Lỗi: {e}")
            return False
    @staticmethod
    def delete_product(path, product_id):
        try:
            with open(path, "r", encoding="utf-8") as file:
                lines = file.readlines()

            new_lines = [line for line in lines if not line.startswith(product_id + ";")]

            if len(new_lines) == len(lines):
                print(f"Không tìm thấy sản phẩm có ID: {product_id}")
                return False


            with open(path, "w", encoding="utf-8") as file:
                file.writelines(new_lines)

            print(f"Đã xóa sản phẩm có ID: {product_id}")
            return True

        except FileNotFoundError:
            print("File không tồn tại!")
            return False
        except Exception:
            traceback.print_exc()
            return False



