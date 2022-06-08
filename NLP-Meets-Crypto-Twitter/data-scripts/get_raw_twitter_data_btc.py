import json
import time
import requests
import pandas as pd
from datetime import date, timedelta

def main():
	start_date = date(2020, 1, 1)
	end_date = date(2022, 1, 2)
	delta = timedelta(days=1)
	dates = []

	while start_date <= end_date:
		dates.append(start_date.strftime("%Y-%m-%d"))
		start_date += delta

	print("getting tweets")
	get_twitter_data(dates)
	print("done")


def get_twitter_data(dates):
	data = []
	for i in range(len(dates)-1):
		start_date = dates[i]
		end_date = dates[i+1]
		url  = "http://localhost:8080/btc?key=" + start_date + "," + end_date
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
	df.to_csv('btc_keyword_raw_tweets.csv')

def clean(dd):
	if 'data' not in dd:
		return ""
	tweet = ""
	for i in range(len(dd['data'])):
		tweet += dd['data'][i]['text']
	return tweet



if __name__ == '__main__':
	main()