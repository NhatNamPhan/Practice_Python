class Student():
    def __init__(self, student_id, name, grades:list):
        self.student_id = student_id
        self.name = name
        self.grades = grades
    def add_grades(self,grade):
        self.grades.append(grade)
    def get_average(self):
        return sum(self.grades)/len(self.grades)

class Classroom():
    def __init__(self, class_name, students:list[Student] = None):
        self.class_name = class_name
        self.students = students if students is not None else []
    def add_student(self,student):
        self.students.append(student)
    def get_class_average(self):
        return sum(stu.get_average() for stu in self.students)/len(self.students)
    def display_students(self):
        print(f"Danh sách sinh viên lớp {self.class_name}")
        print("-"*28)
        for stu in self.students:
            print(f"Mã sinh viên: {stu.student_id}")
            print(f"Tên sinh viên: {stu.name}")
            print(f"Điểm trung bình: {stu.get_average()}")
            print("-"*28)

def menu():
    classrooms = []
    classroom = None
    while True:
        print("\n1. Thêm sinh viên vào lớp")
        print("2. Điểm trung bình của cả lớp")
        print("3. Danh sách sinh viên các lớp")
        print("4. Thoát")
        choose = int(input("Chọn chức năng:"))
        if choose == 1:
            class_name = input("Nhập lớp:")
            classroom = Classroom(class_name)
            while True:
                id = input("Nhập mã sinh viên:")
                name = input("Nhập tên sinh viên:")
                toan = float(input("Nhập điểm toán:"))
                ly = float(input("Nhập điểm lý:"))
                hoa = float(input("Nhập điểm hóa:"))
                # grades = list(map(float, input("Nhập điểm các môn toán, lý, hóa: ").split()))
                grades = [toan,ly,hoa]
                student = Student(id,name,grades)
                classroom.add_student(student)
                more = input("Nhập thêm sinh viên(y/n)?")
                if more.lower() != 'y':
                    break
            classrooms.append(classroom)
        elif choose == 2:
            if not classrooms:
                print("Chưa có lớp nào!!!")
            else:
                for classroom in classrooms:
                    print(f"Điểm trung bình của lớp {classroom.class_name}: {classroom.get_class_average()}")
        elif choose == 3:
            if not classrooms:
                print("Chưa có lớp nào!!!")
            else:
                for classroom in classrooms:
                    classroom.display_students()
        elif choose == 4:
            print("Tạm biệt!!!")
            break
        else: print("Lựa chọn không hợp lệ")

menu()
                    
                