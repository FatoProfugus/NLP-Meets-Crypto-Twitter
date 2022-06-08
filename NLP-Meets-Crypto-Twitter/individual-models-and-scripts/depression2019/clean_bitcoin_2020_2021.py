import pandas as pd

def main():
	df = pd.read_csv('bitcoin_2020_2021.csv')
	df = clean(df)
	df.to_csv('bitcoin_clean_2020_2021.csv')

def clean(df):
	df = df.iloc[::-1]
	df.iloc[:]['Open'] = df.iloc[:]['Open']/100000
	df.iloc[:]['High'] = df.iloc[:]['High']/100000
	df.iloc[:]['Low'] = df.iloc[:]['Low']/100000
	df.iloc[:]['Close'] = df.iloc[:]['Close']/100000
	df.iloc[:]['Volume'] = df.iloc[:]['Volume']/100000000000
	df.iloc[:]['Market Cap'] = df.iloc[:]['Market Cap']/1000000000000
	return df
	

if __name__ == '__main__':
	main()