from datetime import datetime
from collections import defaultdict

class Order:
    def __init__(self, order_id, customer_id, amount, order_date):
        self.order_id = order_id
        self.customer_id = customer_id
        self.amount = amount
        self.order_date = order_date  

orders = [
    Order("O001", "C001", 100.0, "2024-01-15"),
    Order("O002", "C002", 200.0, "2024-01-20"),
    Order("O003", "C001", 150.0, "2024-02-10"),
    Order("O004", "C002", 300.0, "2024-02-25"),
    Order("O005", "C001", 50.0, "2024-01-30"),
]


spending = defaultdict(lambda: defaultdict(float))

for order in orders:
    order_month = datetime.strptime(order.order_date, "%Y-%m-%d").month
    spending[order.customer_id][order_month] += order.amount


for customer_id in spending:
    print(f"Khách hàng {customer_id}:")
    for month in sorted(spending[customer_id]):
        print(f"  Tháng {month}: {spending[customer_id][month]} đ")
