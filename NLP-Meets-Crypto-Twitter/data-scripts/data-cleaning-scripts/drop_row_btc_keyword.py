import pandas as pd

def main():
	df = pd.read_csv('btc_keyword_raw_tweets.csv')
	df = df.iloc[0:len(df)-1][:]
	df.to_csv('btc_keyword_raw_tweets.csv')


if __name__ == '__main__':
	main()