import pandas as pd

#Câu 1:
df = pd.read_csv('../Day30/TOEIC_Points.csv')
df.set_index('Tên',inplace=True)
#print(df)
#Câu 2:
def reward(diem):
    if diem >= 800:
        return ('1,000,000 VND')
    elif diem >= 750:
        return ('700,000 VND')
    elif diem >= 700:
        return ('500,000 VND')
    else: return ('300,000 VND')
df['Thưởng'] = df['Điểm TOEIC'].apply(reward)
#Câu 3:
task_3 = df.loc[(df['Thành phố'] == 'TP.Hồ Chí Minh') & (df['Điểm TOEIC']>720), ['Điểm TOEIC','Thưởng']]
#print(task_3)
#Câu 4:
task_4 = df.sort_values('Điểm TOEIC', ascending=False)
print(task_4.head(3))
#Câu 5:
#df['Thưởng'] = df['Thưởng'].replace(r'[^\d.]', '', regex=True).astype(float)
df['Thưởng'] = df['Thưởng'].str.replace('[^0-9]', '', regex=True).astype(int)
task_5 = df['Thưởng'].sum()
print(task_5)


