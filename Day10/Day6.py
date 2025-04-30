# list_stu = []
# n = int(input("Nhập số sinh viên: "))
# for i in range(n):
#     print(f"\nHọc sinh thứ {i+1}")
#     student = {
#         "name": input("Tên sinh viên: "),
#         "score": {
#             "toan": float(input("Điểm toán: ")),
#             "ly": float(input("Điểm lý: ")),
#             "hoa": float(input("Điểm hóa: "))
#         }
#     }
#     avg = sum(student["score"].values()) / len(student["score"])
#     student["avg"] = avg  

#     if avg > 8.0:
#         student["rank"] = "Giỏi"
#     elif avg > 6.5:
#         student["rank"] = "Khá"
#     elif avg > 5.0:
#         student["rank"] = "Trung bình"
#     else:
#         student["rank"] = "Yếu"

#     list_stu.append(student)

# sort_list = sorted(list_stu, key=lambda sv: sv["avg"], reverse=True)

# print("\n----- Danh sách học sinh -----")
# for sv in sort_list:
#     print(f"Tên sinh viên: {sv['name']}")
#     print(f"Điểm trung bình: {sv['avg']:.2f}")
#     print(f"Xếp loại: {sv['rank']}")
#     print("----------------------------")


def nhap_diem():
    return {
        "toan": float(input("Điểm toán: ")),
        "ly": float(input("Điểm lý: ")),
        "hoa": float(input("Điểm hóa: "))
    }

def tinh_trung_binh(score):
    return sum(score.values()) / len(score)

def xep_loai(avg):
    if avg > 8.0:
        return "Giỏi"
    elif avg > 6.5:
        return "Khá"
    elif avg > 5.0:
        return "Trung bình"
    else:
        return "Yếu"

def nhap_danh_sach_sv():
    list_stu = []
    n = int(input("Nhập số sinh viên: "))
    for i in range(n):
        print(f"\nHọc sinh thứ {i+1}")
        name = input("Tên sinh viên: ")
        score = nhap_diem()
        avg = tinh_trung_binh(score)
        rank = xep_loai(avg)
        student = {
            "name": name,
            "score": score,
            "avg": avg,
            "rank": rank
        }
        list_stu.append(student)
    return list_stu

def in_danh_sach(list_stu):
    print("\n----- Danh sách học sinh -----")
    sort_list = sorted(list_stu, key=lambda sv: sv["avg"], reverse=True)
    for sv in sort_list:
        print(f"Tên sinh viên: {sv['name']}")
        print(f"Điểm trung bình: {sv['avg']:.2f}")
        print(f"Xếp loại: {sv['rank']}")
        print("-"*28)

def dem_rank(list_stu):
    gioi=kha=tb=yeu = 0
    for sv in list_stu:
        if sv['rank'] == "Giỏi":
            gioi +=1
        elif sv['rank'] == "Khá":
            kha +=1
        elif sv['rank'] == "Trung bình":
            tb +=1
        else: yeu +=1
    print("\n----- Thống kê xếp loại -----")
    print("Số sinh viên Giỏi là: ",gioi)
    print("Số sinh viên Khá là: ",kha)
    print("Số sinh viên Trung bình là: ",tb)
    print("Số sinh viên Yếu là: ",yeu)

danh_sach = nhap_danh_sach_sv()
in_danh_sach(danh_sach)
dem_rank(danh_sach)

