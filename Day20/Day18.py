import re
class Customer():
    def __init__(self, name, age, address, phone):
        self.name = name
        self.age = age 
        self.address = address
        self.phone = phone
class ManagerCustomer():
    def __init__(self):
        self.customer = []
    def add_customer(self,customer):
        self.customer.append(customer)
    def display_18_30_age(self):
        matches = [cus for cus in self.customer if 18 <= cus.age <= 30]
        print("Danh sách khách hàng từ 18 đến 30 tuổi")
        for cus in matches:
            print(f"Tên khách hàng: {cus.name}")
            print(f"Tuổi: {cus.age}")
            print(f"Địa chỉ: {cus.address}")
            print(f"Số điện thoại: {cus.phone}")
    def total_customer_age(self):
        total_18_25 = len([cus for cus in self.customer if 18<= cus.age <=25])
        total_26_30 = len([cus for cus in self.customer if 26<= cus.age <=30])
        total_30_up = len([cus for cus in self.customer if 30< cus.age])
        print(f"Số lượng khách hàng trong độ tuổi 18 đến 25: {total_18_25}")
        print(f"Số lượng khách hàng trong độ tuổi 26 đến 30: {total_26_30}")    
        print(f"Số lượng khách hàng trong độ tuổi 30 trở lên: {total_30_up}")  
    def check_phone(self):
        valid_customer = [cus for cus in self.customer if re.fullmatch(r'\d{10}', cus.phone)]
        if not valid_customer:
            print("Không có khách hàng có số điện thoại hợp lệ(xxx-xxx-xxxx)")
        else:
            print("Danh sách khách hàng có số điện thoại hợp lệ:")
            for cus in valid_customer:
                formatted_phone = f"{cus.phone[:3]}-{cus.phone[3:6]}-{cus.phone[6:]}"
                print(f"Tên khách hàng: {cus.name}")
                print(f"Tuổi: {cus.age}")
                print(f"Địa chỉ: {cus.address}")
                print(f"Số điện thoại: {formatted_phone}")
def menu():
    manager = ManagerCustomer()
    while True:
        print("\n1. Thêm khách hàng mới")
        print("2. Danh sách khách hàng độ tuổi từ 18 đến 30")          
        print("3. Số lượng khách hàng ở mỗi độ tuổi")
        print("4. Danh sách khách hàng có số điện thoại hợp lệ(xxx-xxx-xxxx)")
        print("5. Thoát!!!")   
        choose = int(input("Chọn chức năng:"))
        if choose == 1:
            name = input("Nhập tên khách hàng:")
            age = int(input("Nhập tuổi khách hàng"))
            address = input("Nhập địa chỉ khách hàng:")
            phone = input("Nhập số điện thoại khách hàng:")
            customer = Customer(name,age,address,phone)
            manager.add_customer(customer)
        elif choose == 2:
            manager.display_18_30_age()
        elif choose == 3:
            manager.total_customer_age()
        elif choose == 4:
            manager.check_phone()
        elif choose == 5:
            print("Tạm biệt!!!")
            break
        else: print("Lựa chọn không hợp lệ!!!")
menu()   