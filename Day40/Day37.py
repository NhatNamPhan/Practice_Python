import pandas as pd

data = {
    'Tên': ['Nam', 'An', 'Bình', 'Huyền', 'Trúc', 'Dũng', 'Nam', 'An'],
    'Hoạt động': ['Tình nguyện', 'Câu lạc bộ tiếng Anh', 'Bóng đá', 'Múa', 'Câu lạc bộ tiếng Anh', 'Tình nguyện', 'Tình nguyện', 'Bóng đá'],
    'Ngày tham gia': ['2024-11-10', '2024-12-05', '2025-01-15', '2025-01-20', '2025-01-25', '2025-02-05', '2025-03-10', '2025-03-20'],
    'Số giờ tham gia': [3, 2, 2, 4, 2, 3, 4, 2]
}
df = pd.DataFrame(data)
df['Ngày tham gia'] = pd.to_datetime(df['Ngày tham gia'])

#Câu 1:
print('Câu 1')
task_1 = df.groupby(df['Ngày tham gia'].dt.month)['Số giờ tham gia'].sum()
print(task_1)
#Câu 2:
print('Câu 1')
task_2 = df.groupby(df['Ngày tham gia'].dt.quarter)['Số giờ tham gia'].sum()
print(task_2)
#Câu 3:
print('Câu 3')
df = df.sort_values(by=['Tên', 'Ngày tham gia'])  # Sắp theo tên và thời gian
df['Tổng giờ tích lũy'] = df.groupby('Tên')['Số giờ tham gia'].cumsum()
print(df)
#Câu 4:
print('Câu 4')
task_4 = df.groupby('Hoạt động')['Số giờ tham gia'].sum()
task_4 = task_4[task_4>6]
print(df[df['Hoạt động'].isin(task_4.index)])
#Câu 5:
print('Câu 5')
task_5 = df.groupby('Tên')['Số giờ tham gia'].rank(ascending=False)
print(task_5)
