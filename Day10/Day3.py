email_str = input("Mời nhập email của bạn:")
if '@' in email_str:
    part = email_str.split('@')
    if len(part) == 2 and '.' in part[1]:
        print("Email hợp lệ")
    else:
        print("Email không hợp lệ")
else:
    print("Email không hợp lệ")