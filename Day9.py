def nhap_mon_hoc():
    danh_sach_mon = []
    so_mon = int(input("Nhập số môn học của sinh viên:"))
    for i in range(so_mon):
        ten_mon = input(f"Nhập tên môn học thứ {i+1}:")
        diem_so = float(input(f"Nhập điểm số môn {ten_mon}:"))
        mon_hoc = {
            'ten_mon': ten_mon,
            'diem_so': diem_so
        }
        danh_sach_mon.append(mon_hoc)
    return danh_sach_mon

def tinh_trung_binh(danh_sach_mon):
    tong_diem = sum(mon['diem_so'] for mon in danh_sach_mon)
    return tong_diem/len(danh_sach_mon) if danh_sach_mon else 0

def dem_so_mon(danh_sach_mon):
    return len(danh_sach_mon)

def nhap_danh_sach():
    list_stu = []
    n = int(input("Nhập số sinh viên:"))
    for i in range(n):
        print(f"Sinh viên thứ {i+1}")
        name = input("Nhập tên sinh viên:")
        ds_mon = nhap_mon_hoc()
        avg = tinh_trung_binh(ds_mon)
        student = {
            'name': name,
            'subjects': ds_mon,
            'avg': avg
        }
        list_stu.append(student)
    return list_stu

def in_danh_sach(list_stu):
    print("--------Danh sách học sinh--------")
    sort_list = sorted(list_stu, key=lambda sv: sv['avg'], reverse=True)
    for sv in sort_list:
        print(f"Tên sinh viên: {sv['name']}")
        print(f"Số môn học: {dem_so_mon(sv['subjects'])}")
        for mon in sv['subjects']:
            print(f"{mon['ten_mon']}: {mon['diem_so']}")
        print(f"Điểm trung bình: {sv['avg']:.2f}")
        print("----------------------------")

danh_sach = nhap_danh_sach()
in_danh_sach(danh_sach)
        
    
        
        
        
    