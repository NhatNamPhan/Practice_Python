import pandas as pd

df = pd.DataFrame({
    'Tên': ['Nam', 'An', 'Bình', 'Huyền', 'Trúc', 'Dũng'],
    'Ngành học': ['Kinh tế', 'CNTT', 'Ngôn ngữ', 'Kinh tế', 'Kinh tế', 'CNTT'],
    'Điểm TOEIC': [820, 750, 730, 780, 710, 760],
    'Số giờ hoạt động': [12, 8, 10, 15, 6, 9]
})

#Câu 1:
task_1 = df.groupby('Ngành học')['Điểm TOEIC'].mean()
print(task_1)
#Câu 2: 
task_2 = df.groupby('Ngành học')['Số giờ hoạt động'].sum()
print(task_2)
#Câu 3:
task_3 = task_1[task_1>750] 
print(task_3)
#Câu 4:
task_4 = df.groupby('Ngành học')['Số giờ hoạt động'].sum().sort_values(ascending=False)
print(task_4)
#Câu 5:
task_5 = df.groupby('Ngành học').agg({'Điểm TOEIC':'mean','Số giờ hoạt động':'sum'})
print(task_5)