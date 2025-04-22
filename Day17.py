class Student:
    def __init__(self, name, student_id, score):
        self.name = name
        self.student_id = student_id
        self.score = score

    def __str__(self):
        return f"Tên: {self.name}, MSSV: {self.student_id}, Điểm: {self.score}"

class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def show_gioi_students(self):
        gioi_students = [stu for stu in self.students if stu.score >= 8]
        print("\nDanh sách sinh viên loại Giỏi (>= 8):")
        if not gioi_students:
            print("Không có sinh viên loại Giỏi.")
        else:
            for stu in gioi_students:
                print(stu)

    def average_score(self):
        if not self.students:
            return 0
        return sum(stu.score for stu in self.students) / len(self.students)

    def sort_by_score_desc(self):
        sorted_list = sorted(self.students, key=lambda stu: stu.score, reverse=True)
        print("\nDanh sách sinh viên sắp xếp theo điểm giảm dần:")
        for stu in sorted_list:
            print(stu)

def main():
    manager = StudentManager()
    n = int(input("Nhập số lượng sinh viên: "))
    for i in range(n):
        print(f"\nNhập thông tin sinh viên thứ {i + 1}:")
        name = input("Tên: ")
        student_id = input("Mã số sinh viên: ")
        while True:
            try:
                score = float(input("Điểm (0-10): "))
                if 0 <= score <= 10:
                    break
                else:
                    print("Điểm phải trong khoảng 0-10. Nhập lại.")
            except ValueError:
                print("Vui lòng nhập số hợp lệ.")

        student = Student(name, student_id, score)
        manager.add_student(student)

    manager.show_gioi_students()
    print(f"\nĐiểm trung bình của lớp: {manager.average_score():.2f}")
    manager.sort_by_score_desc()

if __name__ == "__main__":
    main()
