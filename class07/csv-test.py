import pandas as pd


df = pd.read_csv('data/data.csv')

df_filtrado = df[df['state'] == 'SP']


print(df_filtrado)

