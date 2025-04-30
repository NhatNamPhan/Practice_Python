class Student():
    def __init__(self, fullname, id_stu, avg_stu, class_stu):
        self.fullname = fullname
        self.id_stu = id_stu
        self.avg_stu = avg_stu
        self.class_stu = class_stu
class ManagerStudent():
    def __init__(self):
        self.students = []
    def add_stu(self,student):
        self.students.append(student)
    def display_list(self):
        if not self.students:
            print("Danh sách rỗng!!!")
            return
        else:
            list_stu = sorted(self.students,key=lambda stu:stu.avg_stu, reverse=True)
            print("--------Danh sách sinh viên--------")
            for stu in list_stu:
                print(f"Sinh viên: {stu.fullname}")
                print(f"Mã sinh viên: {stu.id_stu}")
                print(f"Điểm trung bình: {stu.avg_stu}")
                print(f"Lớp: {stu.class_stu}")
                print("-"*28)
    def max_avg_stu(self):
        if not self.students:
            print("Danh sách rỗng!!!")
            return
        else:
            stu = max(self.students, key=lambda stu:stu.avg_stu)
            print("Sinh viên có điểm trung bình cao nhất:")
            print(f"Sinh viên: {stu.fullname}")
            print(f"Mã sinh viên: {stu.id_stu}")
            print(f"Điểm trung bình: {stu.avg_stu}")
            print(f"Lớp: {stu.class_stu}")
            print("-"*28)
    def avg_class(self):
        if not self.students:
            print("Danh sách rỗng!!!")
            return
        else:
            return sum(stu.avg_stu for stu in self.students)/len(self.students)
    def find_stu_in_class(self,name_class):
        result = [stu for stu in self.students if name_class.lower() == stu.class_stu.lower()]
        if not result:
            print(f"Không tìm thấy sinh viên thuộc lớp {name_class}")
        else:
            print(f"Danh sách sinh viên lớp {name_class}")
            for stu in result:
                print(f"Sinh viên: {stu.fullname}")
                print(f"Mã sinh viên: {stu.id_stu}")
                print(f"Điểm trung bình: {stu.avg_stu}")
                print(f"Lớp: {stu.class_stu}")
                print("-"*28)
def menu():
    manager = ManagerStudent()
    while True:
        print("\n1. Thêm sinh viên")
        print("2. Hiển thị danh sách sinh viên")
        print("3. Sinh viên có điểm trung bình cao nhất")
        print("4. Điểm trung bình của cả lớp")
        print("5. Tìm kiếm danh sách lớp")
        print("6. Thoát")
        choose  = int(input("Chọn chức năng:"))
        if choose == 1:
            fullname = input("Nhập tên sinh viên:")
            id_stu = input("Nhập mã sinh viên:")
            avg_stu = float(input("Nhập điểm trung bình sinh viên:"))
            class_stu = input("Nhập lớp của sinh viên:")
            stu = Student(fullname,id_stu,avg_stu,class_stu)
            manager.add_stu(stu)
        elif choose == 2:
            manager.display_list()
        elif choose == 3:
            manager.max_avg_stu()
        elif choose == 4:
            print(f"Điểm trung bình của cả lớp là: {manager.avg_class():.2f}")
        elif choose == 5:
            name_class = input("Nhập lớp:")
            manager.find_stu_in_class(name_class)
        elif choose == 6:
            print("Tạm biệt!!!")
            break
        else: print("Lựa chọn không hợp lệ!!!")
        
menu()