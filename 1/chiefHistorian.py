import pandas as pd

data = pd.read_csv('data.tsv', sep="\t")

firstList = data.iloc[:,0].sort_values().values
secondList = data.iloc[:,1].sort_values().values

df = pd.DataFrame()
df['col1'] = firstList
df['col2'] = secondList
df['result'] = df['col1'] - df['col2']
print(df['result'].abs().sum())