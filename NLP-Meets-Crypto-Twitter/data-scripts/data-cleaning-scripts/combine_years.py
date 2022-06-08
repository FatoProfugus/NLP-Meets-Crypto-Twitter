import pandas as pd

profiles = ['SBF_FTX', 'depression2019', 'ThinkingBitmex', \
    'profplum99', 'lightcrypto', 'ThinkingUSD', 'CryptoKaleo', \
    'zhusu', 'cobie', 'elonmusk']


def main():
	for profile in profiles:
		df1 = pd.read_csv(profile + '_2020.csv')
		df2 = pd.read_csv(profile + '_2021.csv')
		df = df1.append(df2)
		df.to_csv(profile + '.csv')


if __name__ == '__main__':
	main()