import pandas as pd

#Câu 1:
df = pd.read_csv('../Day30/TOEIC_Points.csv')
df.set_index('Tên',inplace=True)
print(df)
#Câu 2:
task_2 = df.loc[(df['Thành phố']== 'Hà Nội') & (df['Điểm TOEIC'] > 720)]
print(task_2)
#Câu 3:
task_3 = df['Thành phố'].value_counts()
print(task_3)
#Câu 4:
task_4 = df[df['Điểm TOEIC']>750]['Tuổi'].mean()
print(task_4)
#Câu 5:
def xep_loai(diem):
    if diem >= 800:
        return 'Xuất sắc'
    elif diem >= 750:
        return 'Tốt'
    elif diem >= 700:
        return 'Khá'
    else: return 'Trung bình'

df['Xếp loại'] = df['Điểm TOEIC'].apply(xep_loai)
print(df)
