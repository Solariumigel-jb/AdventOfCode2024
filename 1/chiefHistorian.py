import numpy as np
import pandas as pd

data = pd.read_csv('data.tsv', sep="\t")

firstList = data.iloc[:,0].sort_values().values
secondList = data.iloc[:,1].sort_values().values

df = pd.DataFrame()
df['col1'] = firstList
df['col2'] = secondList
df['result'] = df['col1'] - df['col2']
df['countLeft'] = [np.count_nonzero(secondList == x) for x in firstList]
df['result2'] = df['col1'] * df['countLeft']
print(df['result'].abs().sum())

print(df['result2'].sum())