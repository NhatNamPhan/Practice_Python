import pandas as pd

df_new = pd.DataFrame({
    'Tên':['Trúc','Dũng'],
    'Tuổi':[22,23],
    'Thành phố':['Hà Nội','TP.Hồ Chí Minh'],
    'Điểm TOEIC':[730,710]
})

#df_new.to_csv('TOEIC_Points.csv', mode='a',header=False,index=False)
df = pd.read_csv('TOEIC_Points.csv')
#Câu 1:
df.set_index('Tên',inplace=True)
#Câu 2:
#print(df.loc[df['Điểm TOEIC'] > 750])
#Câu 3:
count_by_city = df['Thành phố'].value_counts()
print(count_by_city)
#Câu 4:
avg_age_hcm = df[df['Thành phố'] == 'TP.Hồ Chí Minh']['Tuổi'].mean()
print(f'Tuổi trung bình của các bạn ở Tp.Hồ Chí Minh là: {avg_age_hcm}')
#Câu 5:
def phan_loai(diem):
    if diem >= 800:
        return 'Xuất sắc'
    elif diem >= 750:
        return 'Tốt'
    elif diem >= 700:
        return 'Khá'
    else: return 'Trung bình'
    
df['Xếp loại'] = df['Điểm TOEIC'].apply(phan_loai)
print(df)

