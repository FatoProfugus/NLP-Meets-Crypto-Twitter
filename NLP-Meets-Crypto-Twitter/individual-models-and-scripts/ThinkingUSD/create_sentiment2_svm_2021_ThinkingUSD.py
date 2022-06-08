import io
import sys
import csv
import numpy as np
import pandas as pd

from gensim.models import Word2Vec
from gensim.models import KeyedVectors

from sklearn.svm import SVC

def main():
	embedding_sizes = [100]

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
			X.append(x)
			continue
		sentence += words.split()
		for word in sentence:
			if word in wv:
				x += wv[word]
		X.append(x)
	return np.asarray(X)

def save_sentiment(y_prediction, embedding_size):
	df = pd.DataFrame(y_prediction,columns=['label'])
	df.to_csv('svm2_' + str(embedding_size) + '_sentiment.csv')

def train_model(embedding_size):
	wv = Word2Vec.load('2021_word2vec_ThinkingUSD' + str(embedding_size)+ '.model').wv

	print("starting embedding_size " + str(embedding_size))
	print("before gen_input")
	df = pd.read_csv('ThinkingUSD.csv')
	X_train = gen_input(wv, df[366:366+304], embedding_size)
	X_test = gen_input(wv, df[366+304:len(df)-14], embedding_size)
	print('X_train len ' + str(len(X_train)))
	print('X_test len ' + str(len(X_test)))
	print("after gen_input")

	print("before gen_labels")
	df = pd.read_csv('labels_2.csv')
	y_train = gen_labels(df[366:366+304])
	y_test = gen_labels(df[366+304:len(df)])
	print('y_train len ' + str(len(y_train)))
	print('y_test len ' + str(len(y_test)))
	print("after gen_labels")

	# training algorithm
	print("before training svm")
	svm_model_linear = SVC(kernel='linear').fit(X_train, y_train)
	print("after training svm")

	# prediction code
	print("before prediction")
	y_train_prediction = svm_model_linear.predict(X_train)
	y_prediction = svm_model_linear.predict(X_test)
	print(y_prediction)
	print("after prediction")
	accuracy = svm_model_linear.score(X_test, y_test)
	save_sentiment(y_prediction, embedding_size)
	print('validation accuracy = ' + str(accuracy))
	print("finished embedding_size " + str(embedding_size))
	#y_train_prediction = y_train_prediction.astype(int)
	#y_prediction = y_prediction.astype(int)
	predictions = np.concatenate((y_train_prediction, y_prediction))
	df = pd.DataFrame(predictions, columns=['sentiment'])
	df.to_csv('2021_ThinkingUSD_sentiment2_svm' + str(embedding_size) + '.csv')
	return accuracy



if __name__ == '__main__':
	main()
