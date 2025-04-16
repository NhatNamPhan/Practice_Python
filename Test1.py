class Student():
    def __init__(self, name, class_name):
        self.name = name
        self.class_name = class_name
        self.subjects = {}
    def add_subject(self):
        while True:
            subject = input("Nhập tên môn học (hoặc 'x' để dừng):")
            if subject.lower() == 'x':
                break
            try:
                score = float(input("Nhập điểm số môn học:"))
                self.subjects[subject] = score
            except ValueError:
                print("Vui lòng nhập số hợp lệ")
            
    def calculate_average(self):
        if not self.subjects:
            return 0
        else: 
            return sum(self.subjects.values())/len(self.subjects)

    def get_classification(self):
        avg = self.calculate_average()
        if avg >= 8.0:
            return "Giỏi"
        elif avg >= 6.5:
            return "Khá"
        elif avg >= 5.0:
            return "Trung bình"
        else: return "Yếu"
class StudentManager():
    def __init__(self):
        self.students = []
    def add_student(self, student):
        self.students.append(student)
    def display_list(self):
        if not self.students:
            print("Danh sách sinh viên rỗng")
            return
        else:
            for sv in sorted(self.students ,key= lambda sv: sv.calculate_average(), reverse=True):
                print("\n--------Danh sách sinh viên--------")
                print(f"Tên: {sv.name}")
                print(f"Lớp: {sv.class_name}")
                print(f"Điểm trung bình: {sv.calculate_average():.2f}")
                print(f"Xếp loại: {sv.get_classification()}")
                print('-'*28)
    def max_avg(self):
        if not self.students:
            print("Chưa có sinh viên nào!!!")
            return
        else: 
            max_avg = max(self.students, key= lambda sv: sv.calculate_average())
            print("Sinh viên có điểm trung bình cao nhất")
            print(f"Tên: {max_avg.name}")
            print(f"Lớp: {max_avg.class_name}")
            print(f"Điểm trung bình: {max_avg.calculate_average():.2f}")
            print(f"Xếp loại: {max_avg.get_classification()}")
            print('-'*28)
def menu():
    manager = StudentManager()
    while True:
        print("\n1. Thêm sinh viên ")
        print("2. Hiển thị danh sách")
        print("3. Sinh viên có điểm cao nhất")
        print("4. Thoát")
        chon = input("Chọn chức năng:")
        if chon == '1':
            ten = input("Nhập tên sinh viên:")
            lop = input("Nhập lớp:")
            student = Student(ten,lop)
            student.add_subject()
            manager.add_student(student)
        elif chon == '2':
            manager.display_list()
        elif chon == '3':
            manager.max_avg()
        elif chon == '4':
            print("Tạm biệt!!!")
            break
        else : print("Lựa chọn không hợp lệ")
    
menu()
    