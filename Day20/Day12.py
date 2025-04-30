class Products():
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
class ManagerProduct():
    def __init__(self):
        self.products = []
    def add_product(self, product):
        self.products.append(product)
    def display_list(self):
        if not self.products:
            print("Danh sách rỗng")
            return
        else:
            for pro in sorted(self.products, key=lambda pro:pro.price, reverse=True):
                print("--------Danh sách sản phẩm--------")
                print(f"Sản phẩm: {pro.name}")
                print(f"Giá bán: {pro.price}")
                print(f"Số lượng tồn kho: {pro.quantity}")
                print("-"*28)
    def total_quantity(self):
        if not self.products:
            print("Danh sách rỗng")
            return
        else:
            tong = sum(pro.quantity for pro in self.products)
            print(f"\nTổng số lượng tồn kho: {tong}")
    def max_price(self):
        if not self.products:
            print("Danh sách rỗng")
            return
        else:
            max_price =max(self.products, key=lambda pro:pro.price)
            
            print("\n--------Sản phẩm có giá cao nhất--------")
            print(f"Sản phẩm: {max_price.name}")
            print(f"Giá bán: {max_price.price}")
            print(f"Số lượng tồn kho: {max_price.quantity}")
            print("-"*28)
def menu ():
    manager = ManagerProduct()
    while True:
        print("\n1. Thêm sản phẩm mới")
        print("2. Hiển thị danh sách sản phẩm")
        print("3. Sản phẩm có giá cao nhất")
        print("4. Tổng số lượng hàng tồn kho")
        print("5. Thoát")
        choose = input("Chọn chức năng:")
        if choose == '1':
            name = input("Tên sản phẩm:")
            price = float(input("Giá sản phẩm:"))
            quantity = int(input("Số lượng:"))
            product = Products(name,price,quantity)
            manager.add_product(product)
        elif choose == '2':
            manager.display_list()
        elif choose == '3':
            manager.max_price()
        elif choose == '4':
            manager.total_quantity()
        elif choose == '5': 
            print('Tạm biệt!!!')
            break
        else:
            print("Lựa chọn không hợp lệ!!!")

menu()