import io
import sys
import csv
import numpy as np
import pandas as pd

from gensim.models import Word2Vec
from gensim.models import KeyedVectors

from sklearn.svm import SVC

def main():
	embedding_sizes = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500]

	accuracies = []
	for embedding_size in embedding_sizes:
		acc = train_model(embedding_size)
		accuracies.append(acc)
	print(accuracies)

# helper functions

def gen_labels(df):
	y = list(df.iloc[:]['label'])
	return np.asarray(y)

def gen_input(wv, df, embedding_size):
	X = []
	for i in range(len(df)):
		x = [0] * embedding_size
		sentence = []
		words = df.iloc[i]['Tweets']
		if (pd.isna(words)):
			continue
		sentence += words.split()
		for word in sentence:
			if word in wv:
				x += wv[word]
		X.append(x)
	return np.asarray(X)

def save_sentiment(y_prediction, embedding_size):
	df = pd.DataFrame(y_prediction,columns=['label'])
	df.to_csv('svm6_' + str(embedding_size) + '_sentiment.csv')

def train_model(embedding_size):
	wv = Word2Vec.load('embedding_models/word2vec_' + str(embedding_size)+ '.model').wv

	print("starting embedding_size " + str(embedding_size))
	print("before gen_input")
	df = pd.read_csv('twitter-data/combined_tweets.csv')
	X_train = gen_input(wv, df[:304], embedding_size)
	X_test = gen_input(wv, df[304:len(df)-14], embedding_size)
	print('X_train len ' + str(len(X_train)))
	print('X_test len ' + str(len(X_test)))
	print("after gen_input")

	print("before gen_labels")
	df = pd.read_csv('labels_2.csv')
	y_train = gen_labels(df[:304])
	y_test = gen_labels(df[304:len(df)-1])
	print('y_train len ' + str(len(y_train)))
	print('y_test len ' + str(len(y_test)))
	print("after gen_labels")

	# training algorithm
	print("before training svm")
	svm_model_linear = SVC(kernel='linear').fit(X_train, y_train)
	print("after training svm")

	# prediction code
	print("before prediction")
	y_prediction = svm_model_linear.predict(X_test)
	print(y_prediction)
	print("after prediction")
	accuracy = svm_model_linear.score(X_test, y_test)
	save_sentiment(y_prediction, embedding_size)
	print('validation accuracy = ' + str(accuracy))
	print("finished embedding_size " + str(embedding_size))
	return accuracy



if __name__ == '__main__':
	main()
