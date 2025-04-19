class Employee():
    def __init__(self, name, position, salary, start_year):
        self.name = name
        self.position = position
        self.salary = salary
        self.start_year = start_year

class Manager_Employ():
    def __init__(self):
        self.employs = []
    def add_employee(self,employ):
        self.employs.append(employ)
    def display_list(self):
        if not self.employs:
            print("Danh sách rỗng!!!")
            return
        else:
            print("\n--------Danh sách nhân viên--------")
            for em in sorted(self.employs, key=lambda em:em.start_year):
                print(f"Tên nhân viên: {em.name}")
                print(f"Vị trí: {em.position}")
                print(f"Lương: {em.salary}")
                print(f"Năm vào làm: {em.start_year}")
                print(f"-"*28)
    def total_salary(self):
        if not self.employs:
            print("Danh sách rỗng!!!")
            return
        else:
            return sum(em.salary for em in self.employs)
    def max_salary(self):
        if not self.employs:
            print("Danh sách rỗng!!!")
            return
        else:
            em = max(self.employs, key= lambda em:em.salary)
            print("Nhân viên có tiền lương cao nhất:\n")
            print(f"Tên nhân viên: {em.name}")
            print(f"Vị trí: {em.position}")
            print(f"Lương: {em.salary}")
            print(f"Năm vào làm: {em.start_year}")
            print(f"-"*28)
    def search_department_head(self):
        if not self.employs:
            print("Danh sách rỗng!!!")
            return
        else:
            employ = [em for em in self.employs if em.position.lower() == "trưởng phòng"]
            if employ:
                for em in employ:
                    print(f"Tên nhân viên: {em.name}")
                    print(f"Vị trí: {em.position}")
                    print(f"Lương: {em.salary}")
                    print(f"Năm vào làm: {em.start_year}")
                    print(f"-"*28)
            else: print("Không tìm thấy trưởng phòng nào")

def menu():
    manager = Manager_Employ()
    while True:
        print("\n 1. Thêm nhân viên mới")
        print("2. Hiển thị danh sách nhân viên")
        print("3. Tổng quỹ lương")
        print("4. Nhân viên có lương cao nhất")
        print("5. Nhân viên có chức vụ Trưởng phòng")
        print("6. Thoát")
        choose = int(input("Chọn chức năng:"))
        if choose == 1:
            name = input("Nhập tên nhân viên:")
            position = input("Nhập vị trí nhân viên:")
            salary = float(input("Nhập tiền lương nhân viên:"))
            start_year = int(input("Nhập năm vào làm:"))
            employ = Employee(name,position,salary,start_year)
            manager.add_employee(employ)
        elif choose == 2:
            manager.display_list()
        elif choose == 3:
            print(f"Tổng số tiền lương phải trả cho nhân viên là: {manager.total_salary()}")
        elif choose == 4:
            manager.max_salary()
        elif choose == 5:
            manager.search_department_head()
        elif choose == 6:
            print("Tạm biệt!!!")
            break
        else: print("Lựa chọn không hợp lệ")

menu()








