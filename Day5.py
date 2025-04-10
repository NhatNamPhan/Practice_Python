# name = input("Nhập tên của sinh viên:")
# toan = float(input("Nhập điểm toán:"))
# ly = float(input("Nhập điểm lý:"))
# hoa = float(input("Nhập điểm hóa:"))
# avg_d = sum([toan,ly,hoa])/ len([toan,ly,hoa])
# if avg_d > 8.0 :
#     rank = "Giỏi"
# elif avg_d > 6.5:
#     rank = "Khá"
# elif avg_d > 5.0:
#     rank = "Trung bình"
# else: 
#     rank = "Yếu"
# print(f"Học sinh: {name}")
# print(f"Điểm trung bình: {avg_d:.2f}")
# print(f"Xếp loại: {rank}")
student = {
    "name": input("Tên học sinh: "),
    "scores": {
        "Toán": float(input("Toán: ")),
        "Lý": float(input("Lý: ")),
        "Hóa": float(input("Hóa: "))
    }
}

# Tính điểm trung bình
avg = sum(student["scores"].values()) / len(student["scores"])

# Xếp loại
if avg >= 8.0:
    student["rank"] = "Giỏi"
elif avg >= 6.5:
    student["rank"] = "Khá"
elif avg >= 5.0:
    student["rank"] = "Trung bình"
else:
    student["rank"] = "Yếu"

# In kết quả
print(f"\nHọc sinh: {student['name']}")
print(f"Điểm trung bình: {avg:.2f}")
print(f"Xếp loại: {student['rank']}")
