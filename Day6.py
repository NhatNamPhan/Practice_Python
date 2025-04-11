list_stu = []
n = int(input("Nhập số sinh viên: "))
for i in range(n):
    print(f"\nHọc sinh thứ {i+1}")
    student = {
        "name": input("Tên sinh viên: "),
        "score": {
            "toan": float(input("Điểm toán: ")),
            "ly": float(input("Điểm lý: ")),
            "hoa": float(input("Điểm hóa: "))
        }
    }
    avg = sum(student["score"].values()) / len(student["score"])
    student["avg"] = avg  

    if avg > 8.0:
        student["rank"] = "Giỏi"
    elif avg > 6.5:
        student["rank"] = "Khá"
    elif avg > 5.0:
        student["rank"] = "Trung bình"
    else:
        student["rank"] = "Yếu"

    list_stu.append(student)

sort_list = sorted(list_stu, key=lambda sv: sv["avg"], reverse=True)

print("\n----- Danh sách học sinh -----")
for sv in sort_list:
    print(f"Tên sinh viên: {sv['name']}")
    print(f"Điểm trung bình: {sv['avg']:.2f}")
    print(f"Xếp loại: {sv['rank']}")
    print("----------------------------")
