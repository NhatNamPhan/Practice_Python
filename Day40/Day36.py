import pandas as pd
from datetime import datetime

data = {
    'Tên': ['Nam', 'An', 'Bình', 'Huyền', 'Trúc', 'Dũng','Nam'],
    'Hoạt động': ['Tình nguyện', 'Câu lạc bộ tiếng Anh', 'Bóng đá', 'Múa', 'Câu lạc bộ tiếng Anh', 'Tình nguyện','Tình nguyện'],
    'Ngày tham gia': ['2024-11-10', '2024-12-05', '2025-01-15', '2025-01-20', '2025-01-25', '2025-02-05','2025-11-10'],
    'Số giờ tham gia': [3, 2, 2, 4, 2, 3,4]
}

df = pd.DataFrame(data)
df['Ngày tham gia'] = pd.to_datetime(df['Ngày tham gia'])

#Câu 1:
print('Câu 1\n')
task_1 = df.groupby('Tên')['Số giờ tham gia'].sum().sort_values(ascending=False)
print(task_1)
#Câu 2:
print('Câu 2\n')
task_2 = df.groupby('Hoạt động')['Số giờ tham gia'].sum()
print(task_2)
#Câu 3:
print('Câu 3\n')
task_3 = df.loc[(df['Ngày tham gia'].dt.month == 1)  & (df['Ngày tham gia'].dt.year == 2025)]
print(task_3)
#Câu 4:
print('Câu 4\n')
def type_activity(activity):
    if activity.find('Câu lạc bộ') != -1:
        return 'CLB'
    elif activity.find('Tình nguyện') != -1:
        return 'Volunteer'
    else: return 'Khác'
df['Loại hoạt động'] = df['Hoạt động'].apply(type_activity)
print(df)
#Câu 5:
print('Câu 5\n')
task_5 = df.groupby('Tên')['Ngày tham gia'].max().reset_index()
print(task_5)

