year_ck = int(input("Mời nhập năm:"))
if (year_ck % 4 == 0 and year_ck % 100 != 0) or year_ck % 400 == 0:
    print("Đây là năm nhuận")
else:
    print("Đây không phải là năm nhuận")