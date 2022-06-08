import json
import time
import requests
import pandas as pd
from datetime import date, timedelta

profiles = ['SBF_FTX', 'depression2019', 'ThinkingBitmex', \
    'profplum99', 'lightcrypto', 'ThinkingUSD', 'CryptoKaleo', \
    'zhusu', 'cobie', 'elonmusk']

def main():
	start_date = date(2020, 1, 1)
	end_date = date(2021, 1, 2)
	delta = timedelta(days=1)
	dates = []

	while start_date <= end_date:
		dates.append(start_date.strftime("%Y-%m-%d"))
		start_date += delta

	for profile in profiles:
		print("getting data for " + profile)
		get_twitter_data(profile, dates)
		print("done")


def get_twitter_data(profile, dates):
	data = []
	for i in range(len(dates)-1):
		start_date = dates[i]
		end_date = dates[i+1]
		url  = "http://localhost:8080/profile?key=" + profile + "," + start_date + "," + end_date
		r = requests.get(url)
		jstr = r.content.decode()
		dd = None
		try:
			dd = json.loads(jstr)
		except Exception as e:
			dd = dict()
		tweet = clean(dd)
		data.append([start_date, tweet])
		time.sleep(3.1)
	df = pd.DataFrame(data,columns=['Dates', 'Tweets'])
	df.to_csv(profile+'_2021.csv')

def clean(dd):
	if 'data' not in dd:
		return ""
	tweet = ""
	for i in range(len(dd['data'])):
		tweet += dd['data'][i]['text']
	return tweet



if __name__ == '__main__':
	main()