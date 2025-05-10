from datetime import datetime, timedelta
from collections import defaultdict

class Order:
    def __init__(self, customer_id, order_date):
        self.customer_id = customer_id
        self.order_date = datetime.strptime(order_date, "%Y-%m-%d").date()

# Ví dụ danh sách đơn hàng
orders = [
    Order("C001", "2025-04-10"),
    Order("C001", "2025-04-17"),
    Order("C001", "2025-04-24"),
    Order("C001", "2025-05-01"),
    Order("C002", "2025-04-11"),
    Order("C002", "2025-04-11"),
    Order("C002", "2025-04-20"),
    Order("C003", "2025-04-13"),
    Order("C003", "2025-04-25"),
    Order("C003", "2025-05-03"),
]

def active_customers_by_week(orders):
    today = datetime.today().date()
    start_date = today - timedelta(days=28)

    weekly_orders = defaultdict(lambda: set())

    for order in orders:
        if start_date <= order.order_date <= today:
            week_num = ((order.order_date - start_date).days) // 7
            weekly_orders[order.customer_id].add(week_num)

    result = [cid for cid, weeks in weekly_orders.items() if len(weeks) == 4]
    return result

# Kiểm tra
print("Khách hàng mua hàng mỗi tuần trong 4 tuần gần nhất:")
print(active_customers_by_week(orders))
