import pandas as pd

df_major = pd.DataFrame({
    'Tên':['Nam','An','Bình','Huyền','Trúc','Dũng'],
    'Ngành học':['Kinh tế','Công nghệ thông tin','Ngôn ngữ Anh','Quản trị kinh doanh','Kinh tế','Quản trị kinh doanh']
})

#Câu 1:
df_toeic = pd.read_csv('../Day30/TOEIC_Points.csv')
print(df_major)
print(df_toeic)
#Câu 2:
df_merge = pd.merge(df_major,df_toeic, on='Tên',how='inner')
print(df_merge)
#Câu 3:
def rank(score):
    if score >= 800:
        return 'Xuất sắc'
    elif score >= 750:
        return 'Tốt'
    elif score >= 700:
        return 'Khá'
    else: return 'Trung bình'
    
df_merge['Xếp loại'] = df_merge['Điểm TOEIC'].apply(rank)
print(df_merge)
#Câu 4:
task_4 = df_merge.loc[(df_merge['Điểm TOEIC'] >740) & (df_merge['Ngành học'].isin(['Kinh tế','Công nghệ thông tin']))]
print(task_4)
#Câu 5:
task_5 = df_merge['Ngành học'].value_counts()
print(task_5)
#Câu 6:
df_merge.to_csv('merged_result.csv')
