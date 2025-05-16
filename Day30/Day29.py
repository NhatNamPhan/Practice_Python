import pandas as pd


df = pd.read_csv('TOEIC_Points.csv')

#Câu a:
df.set_index('Tên',inplace=True)
print(df)
#Câu b:
print(df.loc['An'])
#Câu c:
print(df.iloc[1])
#Câu d:
print(df.loc['Huyền','Điểm TOEIC'],)
#Câu e:
print(df.loc[df['Điểm TOEIC']> 750])