class Product():
    def __init__(self, product_id:int, name, price:float):
        self.product_id = product_id
        self.name = name
        self.price = price
class OrderItem():
    def __init__(self, product:Product, quantity:int):
        self.product = product
        self.quantity = quantity
    def get_total_price(self) -> float:
        return self.product.price * self.quantity
class Order():
    def __init__(self,order_id:int, order_items: list[OrderItem] = None):
        self.order_id = order_id
        self.order_items = order_items if order_items is not None else []
    def add_item(self,order_item):
        self.order_items.append(order_item)
    def get_total_order(self) -> float:
        return sum(item.get_total_price() for item in self.order_items)
    def display_order(self):
        print(f"Đơn hàng: {self.order_id}")
        print("-"*28)
        for item in self.order_items:
            print(f"Sản phẩm: {item.product.name}")
            print(f"Số lượng: {item.quantity}")
            print(f"Giá: {item.product.price}")
            print(f"Thành tiền: {item.get_total_price()}")
            print("-"*28)
        print(f"Tổng đơn hàng: {self.get_total_order()}")
def menu():
    orders = []
    order = None
    while True:
        print('\n1. Tạo đơn hàng mới')
        print('2. Xem hóa đơn theo ID')
        print('3. Hiển thị tất cả đơn hàng')
        print('4. Thoát')
        choose = int(input("Chọn chức năng:"))
        if choose == 1:
            order_id = int(input("Id đơn hàng:"))
            order = Order(order_id)
            while True:
                product_id = int(input("Id sản phẩm:"))
                name = input("Sản phẩm:")
                price = float(input("Giá sản phẩm:"))
                quantity = int(input("Số lượng:"))
                product = Product(product_id,name,price)
                order_item = OrderItem(product,quantity)
                order.add_item(order_item)
                more = input("Thêm sản phẩm nữa?(y/n)")
                if more.lower() != 'y':
                    break
            orders.append(order)
        elif choose == 2:
            if not orders:
                print("Chưa có đơn hàng nào!!!")
            else: 
                search_id = int(input("Nhập ID đơn hàng cần tìm:"))
                found = False
                for order in orders:
                    if order.order_id == search_id:
                        order.display_order()
                        found = True
                        break
                if not found:
                    print(f'Không tìm thấy đơn hàng có ID {search_id}')
        elif choose == 3:
            if not orders:
                print("Chưa có đơn hàng nào!!!")
            for order in orders:
                order.display_order()
        elif choose == 4:
            print("Tạm biệt!!!")
            break
        else: print("Lựa chọn không hợp lệ!!!")

menu()
            