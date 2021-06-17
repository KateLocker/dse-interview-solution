import pandas as pd

df = pd.read_csv("sample_data.csv")

#print(df.info())

dic = []

for row in df.itertuples():
    dic.append((row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11]))

print(dic)

