import pandas as pd

profiles = ['SBF_FTX', 'depression2019', 'ThinkingBitmex', \
    'profplum99', 'lightcrypto', 'ThinkingUSD', 'CryptoKaleo', \
    'zhusu', 'cobie', 'elonmusk']

def main():
	tweets = []
	for i in range(731):
		tweets.append(all_tweets(i))
	df = pd.DataFrame(tweets,columns=['Tweets'])
	df.to_csv('combined_tweets_2020_2021.csv')

def all_tweets(i):
	tweets = ''
	for profile in profiles:
		df = pd.read_csv(profile + '.csv')
		tweet = df.iloc[i]['Tweets']
		if(type(df.iloc[i]['Tweets']) == float):
			continue
		tweets += tweet
		tweets += ' '
	return tweets


if __name__ == '__main__':
	main()