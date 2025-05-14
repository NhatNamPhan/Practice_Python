import pandas as pd


students = pd.DataFrame({
    'Tên':['Nam','An','Bình','Huyền'],
    'Tuổi':[22,23,21,24],
    'Thành phố':['Hà Nội','TP.Hồ Chí Minh','Đà Nẵng','Cần Thơ'],
    'Điểm TOEIC':[750,800,700,780]
})
#Câu a: Hiển thị toàn bộ DataFrame
print(students)
#Câu b: Hiển thị danh sách các cột
print(students.columns)
#Câu c: Hiển thị dòng đầu tiên và dòng cuối cùng
print('Dòng đầu tiên:')
print(students.head(1))
print('Dòng cuối cùng:')
print(students.tail(1))
#Câu d: Tính tuổi trung bình của các bạn trong bản
avg_age = students['Tuổi'].mean()
print(f'Tuổi trung bình của các bạn là: {avg_age}')
#Câu e: Lọc ra các bạn có điểm TOEIC từ 750 trở lên
more_750 = students[students['Điểm TOEIC'] >= 750]
print('Danh sách các bạn có điểm TOEIC trên 750')
print(more_750)
students.to_csv('TOEIC_Points.csv',index=False, encoding='utf-8-sig')