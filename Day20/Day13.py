class Book():
    def __init__(self, title, author, year, status):
        self.title = title
        self.author = author
        self.year = year
        self.status = status

class LibraryManager():
    def __init__(self):
        self.books = []
    def add_book(self,book):
        self.books.append(book)
    def display_list(self):
        if not self.books:
            print("Danh sách rỗng!!!")
            return
        else:
            print("\n--------Danh sách đầu sách--------")
            for bk in sorted(self.books, key=lambda bk:bk.year, reverse=True):
                print(f"Tên sách: {bk.title}")
                print(f"Tác giả: {bk.author}")
                print(f"Năm xuất bản: {bk.year}")
                print(f"Trạng thái: {bk.status}")
                print(f"-"*28)
    def search_book(self,search_title):
        if not self.books:
            print("Danh sách rỗng!!!")
            return
        else:
            matches = [bk for bk in self.books if search_title.lower() in bk.title.lower()]
            if matches:
                for bk in matches:
                    print(f"Tên sách: {bk.title}")
                    print(f"Tác giả: {bk.author}")
                    print(f"Năm xuất bản: {bk.year}")
                    print(f"Trạng thái: {bk.status}")
                    print(f"-"*28)
            else: print("Không tìm thấy sách bạn muốn tìm")
    def borrow_book(self,book):
        if not self.books:
            print("Danh sách rỗng!!!")
            return
        else:
            matches = next((bk for bk in self.books if book.lower() == bk.title.lower()),None)
            if not matches:
                print("Không tìm thấy sách muốn mượn!!!")
            elif matches.status == "borrowed":
                print("Sách này đã có người mượn!!!")
            else:
                matches.status = "borrowed"
                print("Mượn sách thành công!!!")
                
    def return_book(self, book):
        if not self.books:
            print("Danh sách rỗng!!!")
            return
        else:
            matches = next((bk for bk in self.books if book.lower() == bk.title.lower()),None)
            if not matches:
                print("Không tìm thấy sách cần trả")
            elif matches.status == "available":
                print("Sách này chưa được mượn")
            else:
                matches.status = "available"
                print("Trả sách thành công!!!")
                
def menu():
    manager = LibraryManager()
    while True:
        print("\n1. Thêm sách mới")
        print("2. Hiển thị danh sách các đầu sách")
        print("3. Tìm sách theo tiêu đề")
        print("4. Mượn sách")
        print("5. Trả sách")
        print("6. Thoát")
        choose = int(input("Nhập lựa chọn chức năng:"))
        if choose == 1:
            title = input("Nhập tên sách:")
            author = input("Nhập tên tác giả:")
            year = int(input("Nhập năm xuất bản:"))
            status = "available"
            book = Book(title,author,year,status)
            manager.add_book(book)
        elif choose == 2:
            manager.display_list()
        elif choose == 3:
            search_bk = input("Nhập tên sách cần tìm:")
            manager.search_book(search_bk)
        elif choose == 4:
            borrow_bk = input("Nhập tên sách muốn mượn:")
            manager.borrow_book(borrow_bk)
        elif choose == 5:
            return_bk = input('Nhập tên sách muốn trả:')
            manager.return_book(return_bk)
        elif choose == 6:
            print("Tạm biệt!!!")
            break
        else: print("Lựa chọn không hợp lệ")

menu()
