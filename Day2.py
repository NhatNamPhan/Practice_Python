number = int(input("Mời nhập số:"))
if number % 2 == 0:
    message = "Đây là số chẵn"
else:
    message = "Đây là số lẻ"
if number < 0:
    message += " và là số âm"
print(message)

    