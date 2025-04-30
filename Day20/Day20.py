class Product():
    def __init__(self,product_id, name, category, price, quantity):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity
class Inventory():
    def __init__(self):
        self.products = []
    def add_product(self,product):
        self.products.append(product)
    def remove_product(self,product_id):
        self.products = [pro for pro in self.products if pro.product_id != product_id]
    def update_quantity(self,product_id,quantity):
        for pro in self.products:
            if product_id == pro.product_id:
                pro.quantity = quantity
                return
    def display_inventory(self):
        print("Danh sách hàng tồn kho")
        print("-"*28)
        for pro in self.products:
            print(f"ID sản phẩm: {pro.product_id}")
            print(f"Sản phẩm: {pro.name}")
            print(f"Loại sản phẩm: {pro.category}")
            print(f"Giá bán: {pro.price}")
            print(f"Số lượng: {pro.quantity}")
            print("-"*28)
    def filter_by_category(self,category):
        result = [pro for pro in self.products if pro.category.lower() == category.lower()]
        print(f"Danh sách sản phẩm thuộc loại sản phẩm {category}")
        for pro in result:
            print(f"ID sản phẩm: {pro.product_id}")
            print(f"Sản phẩm: {pro.name}")
            print(f"Loại sản phẩm: {pro.category}")
            print(f"Giá bán: {pro.price}")
            print(f"Số lượng: {pro.quantity}")
    def filter_low_stock(self,threshold):
        result = [pro for pro in self.products if pro.quantity < threshold]
        print("Danh sách sản phẩm sắp hết hàng")
        for pro in result:
            print(f"ID sản phẩm: {pro.product_id}")
            print(f"Sản phẩm: {pro.name}")
            print(f"Loại sản phẩm: {pro.category}")
            print(f"Giá bán: {pro.price}")
            print(f"Số lượng: {pro.quantity}")
def menu():
    inventory = Inventory()
    while True:
        print("\n1. Thêm sản phẩm mới kho")
        print("2. Xóa sản phẩm theo ID")
        print("3. Câp nhật số lượng tồn kho")
        print("4. Hiển thị toàn bộ sản phẩm")
        print("5. Hiển thị các sản phẩm theo loại sản phẩm")
        print("6. Hiển thị sản phẩm sắp hết hàng")
        print("7. Thoát")
        choose = int(input("Chọn chức năng:"))
        if choose == 1:
            product = input("Nhập ID sản phẩm")
            name = input("Nhập tên sản phẩm:")
            category = input("Nhập loại sản phẩm:")
            price = float(input("Nhập giá sản phẩm:"))
            quantity = int(input("Nhập số lượng:"))
            product = Product(product,name,category,price,quantity)
            inventory.add_product(product)
        elif choose == 2:
            remove_pro = input("Nhập ID sản phẩm cần xóa")
            inventory.remove_product(remove_pro)
        elif choose == 3:
            pro = input("Nhập ID sản phẩm cần cập nhât:")
            update_quantity  = int(input("Nhập số lượng cập nhật:"))
            inventory.update_quantity(pro,update_quantity)
        elif choose == 4:
            inventory.display_inventory()
        elif choose == 5:
            category = input("Nhập loại sản phẩm cần hiển thị")
            inventory.filter_by_category(category)
        elif choose == 6:
            threshold = int(input("Nhập ngưỡng hết hàng:"))
            inventory.filter_low_stock(threshold)
        elif choose == 7:
            print("Tạm biệt!!!")
            break
        else: print("Lựa chọn không hợp lệ!!!")
    
menu()       