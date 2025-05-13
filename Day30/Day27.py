import pandas as pd

data = {
    'order_id':[101,102,103,104,105],
    'customer':['An','Ni','Nam','Tâm','Huy'],
    'product':['Bút','Vở','Sách','Cặp','Kéo'],
    'quantity':[1,4,6,80,10],
    'price':[23,12,56,24,124],
    'order_date': ['2024-01-01', '2024-01-02', '2024-01-02', '2024-01-03', '2024-01-04']
}
df = pd.DataFrame(data)
df['order_date'] = pd.to_datetime(df['order_date'])
#Câu 1: Hiển thị 5 dòng 
print("1. 5 dòng đầu tiên:")
print(df.head())
#Câu 2: Tính tổng số lượng và tổng doanh thu (quantity*price) cho mỗi khách hàng (customer)
df['total'] = df['quantity'] * df['price']
customer_summary = df.groupby('customer').agg({
    'quantity': 'sum',
    'total': 'sum'
}).reset_index()
print("\n2. Tổng số lượng và doanh thu của mỗi khách hàng:")
print(customer_summary)
# Câu 3: Tổng doanh thu theo từng ngày
daily_revenue = df.groupby('order_date')['total'].sum().reset_index()
print("\n3. Tổng doanh thu theo từng ngày:")
print(daily_revenue)

# Câu 4: Trung bình số lượng sản phẩm bán ra của mỗi loại sản phẩm
avg_quantity_by_product = df.groupby('product')['quantity'].mean().reset_index()
print("\n4. Trung bình số lượng sản phẩm bán ra theo sản phẩm:")
print(avg_quantity_by_product)

# Câu 5: Danh sách khách hàng theo tổng doanh thu giảm dần
top_customers = customer_summary.sort_values(by='total', ascending=False)
print("\n5. Khách hàng theo tổng doanh thu giảm dần:")
print(top_customers)