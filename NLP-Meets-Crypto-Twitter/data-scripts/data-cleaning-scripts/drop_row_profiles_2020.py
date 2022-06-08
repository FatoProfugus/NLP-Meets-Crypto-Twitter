import pandas as pd

profiles = ['SBF_FTX_2020', 'depression2019_2020', 'ThinkingBitmex_2020', \
    'profplum99_2020', 'lightcrypto_2020', 'ThinkingUSD_2020', 'CryptoKaleo_2020', \
    'zhusu_2020', 'cobie_2020', 'elonmusk_2020']


def main():
	for profile in profiles:
		df = pd.read_csv(profile + '.csv')
		df = df.iloc[0:len(df)-1][:]
		df.to_csv(profile + '.csv')


if __name__ == '__main__':
	main()