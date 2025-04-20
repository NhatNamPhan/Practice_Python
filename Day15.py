class Product():
    def __init__(self, id, name , quantity, purchase_price, selling_price):
        self.id = id
        self.name = name
        self.quantity = quantity
        self.purchase_price = purchase_price
        self.selling_price = selling_price
class ManagerProduct():
    def __init__(self):
        self.products = []
    def add_product(self,product):
        self.products.append(product)
    def display_list(self):
        if not self.products:
            print('Danh sách rỗng!!!')
            return
        else:
            print('\n--------Danh sách sản phẩm--------')
            for pro in self.products:
                print(f'Id Sản phẩm: {pro.id}')
                print(f'Sản phẩm: {pro.name}')
                print(f'Số lượng tồn kho: {pro.quantity}')
                print(f'Giá nhập: {pro.purchase_price}')
                print(f'Giá bán: {pro.selling_price}')
                print('-'*28)
    def total_quantity(self):
        if not self.products:
            print('Danh sách rỗng!!!')
            return
        else: 
            return sum((pro.quantity * pro.purchase_price) for pro in self.products)
    def max_profit(self):
        if not self.products:
            print('Danh sách rỗng!!!')
            return
        else:
            print('Sản phẩm có lợi nhuận cao nhất:')
            pro = max(self.products, key=lambda p:p.selling_price - p.purchase_price)
            print(f'Id Sản phẩm: {pro.id}')
            print(f'Sản phẩm: {pro.name}')
            print(f'Số lượng tồn kho: {pro.quantity}')
            print(f'Giá nhập: {pro.purchase_price}')
            print(f'Giá bán: {pro.selling_price}')
    def profit_above_20_purchase(self):
        if not self.products:
            print('Danh sách rỗng!!!')
            return
        else:
            result = [pro for pro in self.products 
                     if (pro.selling_price - pro.purchase_price) > 0.2 * pro.purchase_price]
            if not result:
                print("Không có sản phẩm nào có lợi nhuận > 20% giá nhập")
                return
            else:               
                print('\nCác sản phẩm có lợi nhuận > 20% giá nhập:')
                for pro in result:
                    print(f'Id Sản phẩm: {pro.id}')
                    print(f'Sản phẩm: {pro.name}')
                    print(f'Giá nhập: {pro.purchase_price}')
                    print(f'Giá bán: {pro.selling_price}')
                    print('-' * 28)
def menu():
    manager = ManagerProduct()
    while True:
        print('\n1. Thêm sản phẩm mới')
        print('2. Hiển thị tất cả sản phẩm')
        print('3. Tổng giá trị tồn kho')
        print('4. Hiển thị sản phẩm có lợi nhuận cao nhất')
        print('5. Hiển thị các sản phẩm có lợi nhuận > 20% giá nhập')
        print('6. Thoát')
        choose = int(input('Nhập chức năng:'))
        if choose == 1:
            id = input('Nhập ID sản phẩm:')
            name = input('Nhập tên sản phẩm:')
            quantity = int(input('Nhập số lượng:'))
            purchase_price = float(input('Nhập giá nhâp:'))
            selling_price = float(input('Nhập giá bán:'))
            product = Product(id,name,quantity,purchase_price,selling_price)
            manager.add_product(product)
        elif choose == 2:
            manager.display_list()
        elif choose == 3:
            print(f'Tổng giá trị tồn kho: {manager.total_quantity()}')
        elif choose == 4:
            manager.max_profit()
        elif choose == 5:
            manager.profit_above_20_purchase()
        elif choose == 6:
            print('Tạm biệt!!')
            break
        else: print('Lựa chọn không hợp lệ!!!')
menu()