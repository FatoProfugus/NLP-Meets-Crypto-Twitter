import pandas as pd

df = pd.read_csv('bitcoin_clean.csv')

def calc_label(i: int) -> int:
	present = df.iloc[i]['Open']
	future = df.iloc[i+14]['Open']
	if(future/present >= 1.1):
		return 1
	elif(future/present >= 1.05):
		return 2
	elif(future/present <= 1.01 and future/present >= 0.99):
		return 3
	elif(future/present > 0.95):
		return 4
	elif(future/present > 0.90):
		return 5
	else:
		return 6

labels = []

for i in range(0,len(df)-14):
	labels.append(calc_label(i))

df = pd.DataFrame(labels, columns = ['label'])

df.to_csv('labels.csv')