import pandas as pd

df_activity = pd.DataFrame({
    'Tên':['Nam','An','Bình','Huyền','Trúc','Dũng'],
    'Hoạt đông':['Tình nguyện','Câu lạc bộ tiếng Anh','Bóng đá','Múa','Câu lạc bộ tiếng Anh','Tình nguyện'],
    'Số giờ tham gia':[12, 8, 10, 15, 6, 9]
})

df_activity.to_csv('Activity.csv',index=False)
#Câu 1: 
df_toeic = pd.read_csv('../Day30/TOEIC_Points.csv')
print(df_toeic)
print(df_activity)
#Câu 2:
df_merged = pd.merge(df_toeic,df_activity,on='Tên',how='inner')
print(df_merged)
#Câu 3:
def rank(score):
    if score >= 800:
        return 'Xuất sắc'
    elif score >= 750:
        return 'Tốt'
    elif score >= 700:
        return 'Khá'
    else: return 'Trung bình'
df_merged['Xếp loại'] = df_merged['Điểm TOEIC'].apply(rank)
print(df_merged)
#Câu 4:
task_4 = df_merged.groupby('Tên')['Số giờ tham gia'].sum().reset_index()
print(task_4)
#Câu 5:
task_5 = df_merged.sort_values(by='Số giờ tham gia',ascending=False).head(1)[['Tên','Số giờ tham gia','Điểm TOEIC']]
print(task_5.head(1))
#Câu 6:
df_merged.to_csv('merged_activity.csv')
