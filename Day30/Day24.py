from datetime import datetime, timedelta
class Customer():
    def __init__(self, customer_id, name, email):
        self.customer_id = customer_id
        self.name = name
        self.email = email
class Order():
    def __init__(self, order_id, customer_id, product_name, amount, date):
        self.order_id = order_id
        self.customer_id = customer_id
        self.product_name = product_name
        self.amount = amount
        self.date = date
class ShopSystem():
    def __init__(self):
        self.customers = []
        self.orders = []
    def add_cus(self, customer):
        self.customers.append(customer)
    def add_order(self, order):
        if not any(c.customer_id == order.customer_id for c in self.customers):
            print(f"Khách hàng với ID {order.customer_id} không tồn tại")
            return
        self.orders.append(order)
    def total_amount_cus(self):
        customer_totals = {}
        for order in self.orders:
            customer_id = order.customer_id
            customer_totals[customer_id] = customer_totals.get(customer_id,0) + order.amount
        for customer_id, total in customer_totals.items():
            print(f"Tổng tiền đã tiền chi của khách hàng {customer_id} là: {total}")
    def cus_most_purchases(self):
        customer_count = {}
        for order in self.orders:
            customer_id = order.customer_id
            customer_count[customer_id] = customer_count.get(customer_id,0) + 1
        max_count = max(customer_count.values())
        top_customers = (cid for cid, count in customer_count.items() if count == max_count)
        print(f"Khách hàng mua nhiều nhất {max_count} lần:")
        for cid in top_customers:
            print(f"Khách hàng {cid}")
    def display_customer(self,day: int):
        today = datetime.now().date()
        start_date = today - timedelta(days=day)
        result = [
            order for order in self.orders
            if start_date <= datetime.strptime(order.date, "%Y-%m-%d").date() <= today
        ]
        for order in result:
            print(f"Mã đơn hàng: {order.order_id}")
            print(f"Mã khách hàng: {order.customer_id}")
            print(f"Sản phẩm: {order.product_name}")
            print(f"Số tiền: {order.amount}")
            print(f"Ngày mua hàng: {order.date}")
            print("-" * 30)
def menu():
    shop = ShopSystem()

    while True:
        print("\n==== MENU ====")
        print("1. Thêm khách hàng")
        print("2. Thêm đơn hàng")
        print("3. Hiển thị tổng tiền mỗi khách hàng")
        print("4. Khách hàng mua nhiều nhất")
        print("5. Hiển thị đơn hàng trong N ngày gần nhất")
        print("0. Thoát")
        choice = input("Chọn chức năng: ").strip()

        if choice == "1":
            customer_id = input("Nhập mã khách hàng: ")
            name = input("Nhập tên: ")
            email = input("Nhập email: ")
            customer = Customer(customer_id, name, email)
            shop.add_cus(customer)

        elif choice == "2":
            order_id = input("Nhập mã đơn hàng: ")
            customer_id = input("Nhập mã khách hàng: ")
            product_name = input("Nhập tên sản phẩm: ")
            amount = float(input("Nhập số tiền: "))
            date = input("Nhập ngày (yyyy-mm-dd): ")
            order = Order(order_id, customer_id, product_name, amount, date)
            shop.add_order(order)

        elif choice == "3":
            shop.total_amount_cus()

        elif choice == "4":
            shop.cus_most_purchases()

        elif choice == "5":
            try:
                day = int(input("Nhập số ngày gần nhất: "))
                shop.display_customer(day)
            except ValueError:
                print("Vui lòng nhập số nguyên!")

        elif choice == "0":
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")
menu()