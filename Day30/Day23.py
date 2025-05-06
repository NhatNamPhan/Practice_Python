from collections import defaultdict
class Employee():
    def __init__(self,employee_id, name, department, salary):
        self.employee_id = employee_id
        self.name = name
        self.department = department
        self.salary = salary
class Company():
    def __init__(self):
        self.employees = []
    def is_empty(self):
        return len(self.employees) == 0
    def add_employee(self,employee):
        self.employees.append(employee)
    def delete_employee(self,id):
        if self.is_empty():
            print("Chưa có nhân viên nào!!!")
            return
        original_len = len(self.employees)
        self.employees = [em for em in self.employees if em.employee_id != id]
        if len(self.employees) == original_len:
            print(f"Không tìm thấy nhân viên với mã {id}")
        else:
            print(f"Đã xóa nhân viên với mã {id}")
    def avg_salary_depart(self):
        if self.is_empty():
            print("Chưa có nhân viên nào!!!")
            return
        departments = defaultdict(list)
        for em in self.employees:
            departments[em.department].append(em.salary)
        for dept,salaries in departments.items():
            avg_salary = sum(salaries)/ len(salaries)
            print(f"Phòng {dept} có lương trung bình: {avg_salary}")
    def display_employee(self):
        if self.is_empty():
            print("Chưa có nhân viên nào!!!")
            return
        print("Danh sách nhân viên trong công ty")
        for em in self.employees:
            print(f"Mã nhân viên: {em.employee_id}")
            print(f"Tên nhân viên: {em.name}")
            print(f"Phòng ban: {em.department}")
            print(f"Lương: {em.salary}")
            print("-"*28)
    def max_salary(self):
        if self.is_empty():
            print("Chưa có nhân viên nào!!!")
            return
        result = max(self.employees, key=lambda em:em.salary)
        print("Nhân viên có lương cao nhất là:")
        print(f"Mã nhân viên: {result.employee_id}")
        print(f"Tên nhân viên: {result.name}")
        print(f"Phòng ban: {result.department}")
        print(f"Lương: {result.salary}")

def menu():
    company = Company()
    while True:
        print("1. Thêm  nhân viên mới:")
        print("2. Xóa nhân viên")
        print("3. Lương trung bình của phòng ban")
        print("4. Hiển thị danh sách nhân viên")
        print("5. Nhân viên có lương nhất")
        print("6. Thoát")
        choose = int(input("Chọn chức năng:"))
        if choose == 1:
            id = input("Nhập mã nhân viên:")
            name = input("Nhập tên nhân viên:")
            department = input("Nhập phòng ban:")
            salary = float(input("Nhập lương:"))
            employee = Employee(id,name,department,salary)
            company.add_employee(employee)
        elif choose == 2:
            id = input("Nhập mã nhân viên:")
            company.delete_employee(id)
        elif choose == 3:
            company.avg_salary_depart()
        elif choose == 4:
            company.display_employee()
        elif choose == 5:
            company.max_salary()
        elif choose == 6:
            print('Tạm biệt!!!')
            break
        else: print("Lựa chọn chức năng không hợp lệ!!!")
menu()