import pandas as pd

df = pd.read_csv('bitcoin_clean_2020_2021.csv')

def calc_label(i: int) -> int:
	present = df.iloc[i]['Open']
	future = df.iloc[i+14]['Open']
	if(future/present >= 1.0):
		return 1
	else:
		return 2

labels = []

for i in range(0,len(df)-14):
	labels.append(calc_label(i))

df = pd.DataFrame(labels, columns = ['label'])

df.to_csv('labels_2.csv')