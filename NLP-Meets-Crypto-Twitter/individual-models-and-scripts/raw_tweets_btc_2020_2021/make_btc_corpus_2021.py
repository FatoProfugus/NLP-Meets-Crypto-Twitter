import pandas as pd

def main():
	tweets = []
	df = pd.read_csv('btc_keyword_raw_tweets.csv')
	for i in range(366, len(df)):
		tweets.append(df.iloc[i]['Tweets'])
	df = pd.DataFrame(tweets,columns=['Tweets'])
	df.to_csv('btc_keyword_corpus_2021.csv')

if __name__ == '__main__':
	main()