from typing import Literal
from datetime import datetime
class Transaction():
    def __init__(self, transaction_id, account_holder, amount:float, type: Literal["deposit","withdraw"], date):
        try:
            datetime.strptime(date,"%Y-%m-%d")
        except ValueError:
            raise ValueError("Ngày phải có định dạng YYYY-MM-DD")
        self.transaction_id = transaction_id
        self.account_holder = account_holder
        self.amount = amount
        self.type = type
        self.date = date
class BankSystem():
    def __init__(self):
        self.transactions = []
    def add_transaction(self,transaction):
        self.transactions.append(transaction)
    def get_total_deposit(self, account):
        return sum(trans.amount for trans in self.transactions if trans.type == "deposit" and trans.account_holder.lower() == account.lower())
    def get_total_withdraw(self, account):
        return sum(trans.amount for trans in self.transactions if trans.type == "withdraw" and trans.account_holder.lower() == account.lower())
    def get_balance(self,account):
        return self.get_total_deposit(account) - self.get_total_withdraw(account)
    def filter_by_month(self, month:int):
        print(f"Danh sách giao dịch trong tháng {month}")
        result = [trans for trans in self.transactions if datetime.strptime(trans.date, "%Y-%m-%d").month == month]
        for tran in result:
            print(f"Mã giao dịch: {tran.transaction_id}")
            print(f"Chủ tài khoản: {tran.account_holder}")
            print(f"Loại giao dịch: {tran.type}")
            if tran.type == "deposit":
                print(f"Tiền giao dịch: +{tran.amount}")
            else: print(f"Tiền giao dịch: -{tran.amount}")
            print(f"Ngày giao dịch: {tran.date}")
def menu():
    bank_system = BankSystem()
    while True:
        print("1. Thêm giao dịch mới")
        print("2. Tổng tiền nạp của chủ tài khoản")
        print("3. Tổng tiền rút của chủ tài khoản")
        print("4. Số dư của tài khoản")
        print("5. In các giao dịch trong tháng")
        print("6. Thoát")
        choose = int(input('Nhập chức năng:'))
        if choose == 1:
            id = input("Nhập mã giao dịch:")
            name = input("Nhập số tài khoản:")
            type = input("Nhập loại giao dịch:")
            amount = float(input('Nhập số tiền giao dịch:'))
            date = input("Nhập ngày giao dịch:")
            trans = Transaction(id,name,amount,type,date)
            bank_system.add_transaction(trans)
        elif choose == 2:
            name = input("Nhập số tài khoản:")
            print(f"Tổng nạp của số tài khoản {name}: {bank_system.get_total_deposit(name)}")
        elif choose == 3:
            name = input("Nhập số tài khoản:")
            print(f"Tổng rút của số tài khoản {name}: {bank_system.get_total_withdraw(name)}")
        elif choose == 4:
            name = input("Nhập số tài khoản:")
            print(f"Số dư của số tài khoản {name}: {bank_system.get_balance(name)}")
        elif choose == 5:
            month = int(input('Nhập tháng giao dịch:'))
            bank_system.filter_by_month(month)
        elif choose == 6:
            print("Tạm biệt!!!")
            break
        else: print("Lựa chọn không hợp lệ!!!")
menu()