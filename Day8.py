def nhap_diem_bat_buoc():
    return{
        "toan": float(input("Điểm toán:")),
        "ly": float(input("Điểm lý:")),
        "hoa": float(input("Điểm hóa:")),
    }
def nhap_diem_tu_chon():
    choice = input("Học sinh này có môn tự chọn không:").strip().lower()
    if choice == "có":
        tu_chon = input("Môn tự chọn là môn:(Sinh hoặc Tin):").strip().lower()
        diem_bat_buoc = nhap_diem_bat_buoc()
        if tu_chon == "sinh":
            return {
                **diem_bat_buoc,
                "sinh": float(input("Điểm sinh:"))
            }
        elif tu_chon == "tin":
            return {
                **diem_bat_buoc,
                "tin": float(input("Điểm tin:"))
            }
        else:
            print("Nhập môn tự chọn không hợp lệ (Chỉ nhận môn Sinh hoặc môn Tin)")
            return nhap_diem_bat_buoc()
    else:
        return nhap_diem_bat_buoc()
def diem_trung_binh(score):
    return sum(score.values())/len(score)
def xep_loại(avg):
    if avg > 8.0:
        return "Giỏi"
    elif avg > 6.5:
        return "Khá"
    elif avg > 5.0:
        return "Trung bình"
    else: return "Yếu"
def nhap_danh_sach():
    n = int(input("Nhập số sinh viên:"))
    list_sv = []
    for i in range(n):
        print(f"Nhập sinh viên thứ {i+1}")
        name = input("Nhập tên sinh viên:")
        class_1 = int(input("Nhập lớp sinh viên:"))
        score = nhap_diem_tu_chon()
        avg = diem_trung_binh(score)
        rank = xep_loại(avg)
        student = {
            'name': name,
            'class': class_1,
            "score": score,
            "avg": avg,
            "rank": rank
        }
        list_sv.append(student)
    return list_sv
def in_danh_sach(list_stu):
    print("--------Danh sách học sinh--------")
    sort_list = sorted(list_stu, key=lambda sv: sv['avg'], reverse=True)
    for sv in sort_list:
        print(f"Tên học sinh: {sv['name']}")
        print(f"Lớp: {sv['class']}")
        print(f"Điểm trung bình: {sv['avg']:.2f}")
        print(f"Xếp loại: {sv['rank']}")
        print("----------------------------")
        
danh_sach = nhap_danh_sach()
in_danh_sach(danh_sach)
    