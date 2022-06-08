import pandas as pd

profiles = ['SBF_FTX', 'depression2019', 'ThinkingBitmex', \
    'profplum99', 'lightcrypto', 'ThinkingUSD', 'CryptoKaleo', \
    'zhusu', 'cobie', 'elonmusk']

def main():
	tweets = []
	for profile in profiles:
		add_tweets(tweets, profile)
	df = pd.DataFrame(tweets,columns=['Tweets'])
	df.to_csv('combined_profiles_corpus_2021.csv')

def add_tweets(tweets, profile):
	df = pd.read_csv(profile + '.csv')
	for i in range(366, len(df)):
		tweets.append(df.iloc[i]['Tweets'])

if __name__ == '__main__':
	main()