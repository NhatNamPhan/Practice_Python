def nhap_san_pham():
    list_prdu = []
    n = int(input("Nhập số lượng sản phẩm:"))
    for i in range(n):
        print(f"Nhập sản phẩm thứ {i+1}")
        name = input('Nhập tên sản phẩm:')
        price = float(input('Nhập giá sản phẩm:'))
        quantity = int(input('Nhập số lượng sản phẩm:'))
        money = price * quantity
        product = {
            'name': name,
            'price': price,
            'quantity': quantity,
            'money': money
        }
        list_prdu.append(product)
    return list_prdu

def in_danh_sach(list_prdu):
    print("-----Danh sách sản phẩm-----")
    sort_list = sorted(list_prdu, key=lambda pro: pro['money'], reverse=True)
    for pro in sort_list:
        print(f"Tên sản phẩm: {pro['name']}")
        print(f"Giá sản phẩm: {pro['price']:.2f}")
        print(f"Số lượng sản phẩm: {pro['quantity']}")
        print(f"Thành tiền: {pro['money']:.2f}")
        print("----------------------------")

def tong_tien(list_prdu):
    return sum(pro['money'] for pro in list_prdu)   
     
danh_sach = nhap_san_pham()
in_danh_sach(danh_sach)
total = tong_tien(danh_sach)
print(f"Tổng tiền tất cả sản phẩm: {total:.2f}")