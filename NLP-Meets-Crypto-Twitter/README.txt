NLP Meets Crypto Twitter

Due to data being large full project repo is available at:
https://drive.google.com/file/d/1CkH-3T32DUnXW7LxNEiv-ulwhWwgLzeN/view?usp=sharing

This project predicts the price of BTC 14 days into the future when given
the current day's BTC data and Twitter data. Please read through "NLPMeetsCryptoTwitter.pdf"
for further details.

Note when running scripts make sure to copy necessary data files to working directory.

Description of folders:

rest-twitter-service
	contains code necessary to collect twitter data

bitcoin-data-and-labels
	contains btc data and labels we are trying to predict

data-scripts
	contains scripts to collect raw twitter data, clean btc data, and produce labels

twitter-data
	contains collected and cleaned twitter data

twitter-data-scripts
	contains twitter data cleaning scripts

embedding-models
	contains saved embedding models

individual-models-and-scripts
	contains ml models trained from indvidual twitter accounts

train-sentiment-model-scripts
	contains scripts for taining sentiment models

sentiment-scripts
	contains scripts necessary to produce sentiment data

sentiment-data
	contains output of sentiment models

train-base-model-scripts
	contains scripts to create base model

train-full-model-scripts
	contains scripts for training full model which produces our best results

