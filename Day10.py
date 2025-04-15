class Contact():
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

class Phonebook():
    def __init__(self):
        self.contacts = []
    def add_contact(self, contact):
        self.contacts.append(contact)
    def search_by_name(self, name):
        name = name.lower()
        return [c for c in self.contacts if c.name.lower() == name]
    def display_contacts(self):
        for contact in sorted(self.contacts, key=lambda c: c.name.lower()):
            print(f"Tên: {contact.name} | SĐT: {contact.phone} | Email: {contact.email}")

def menu():
    pb = Phonebook()
    while True:
        print("\n1. Thêm liên hệ ")
        print("2. Tìm kiếm theo tên")
        print("3. Hiển thị danh bạ")
        print("4. Thoát")
        chon = input("Chọn chức năng:")
        if chon == '1':
            name = input("Nhập tên:")
            phone = input("Nhập số điện thoại:")
            email = input("Nhập email:")
            contact = Contact(name,phone,email)
            pb.add_contact(contact)
        elif chon == '2':
            name = input("Nhập tên cần tìm:")
            kq = pb.search_by_name(name)
            if kq:
                for c in kq:
                    print(f"Tên: {c.name} | SĐT: {c.phone} | Email: {c.email}")
            else: print("Không tìm thấy liên hệ")
        elif chon == '3':
            pb.display_contacts() 
        elif chon == '4':
            print("Tạm biệt!!!")
            break
        else: print("Lựa chọn không hợp lệ")    
        
menu()       