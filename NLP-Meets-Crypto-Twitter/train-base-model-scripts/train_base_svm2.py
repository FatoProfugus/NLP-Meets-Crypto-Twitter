import io
import sys
import csv
import numpy as np
import pandas as pd

from gensim.models import Word2Vec
from gensim.models import KeyedVectors

from sklearn.svm import SVC

def main():
	#embedding_sizes = [50, 100, 150, 200, 250, 300, 350, 450, 500]
	embedding_sizes = [50]

	accuracies = []
	for embedding_size in embedding_sizes:
		acc = train_model(embedding_size)
		accuracies.append(acc)
	print(accuracies)

# helper functions

def gen_labels(df):
	print(df.head)
	y = list(df.iloc[:]['label'])
	return np.asarray(y)

def gen_input(df):
	X = []
	for i in range(len(df)):
		x = []
		x.append(df.iloc[i]['Open'])
		x.append(df.iloc[i]['High'])
		x.append(df.iloc[i]['Low'])
		x.append(df.iloc[i]['Close'])
		x.append(df.iloc[i]['Volume'])
		x.append(df.iloc[i]['Market Cap'])
		X.append(x)
	return np.asarray(X)

def train_model(embedding_size):
	#wv = Word2Vec.load('embedding_models/word2vec_' + str(embedding_size)+ '.model').wv

	print("starting embedding_size " + str(embedding_size))
	print("before gen_input")
	df = pd.read_csv('bitcoin_clean.csv')
	X_train = gen_input(df[:304])
	X_test = gen_input(df[304:len(df)-14-1])
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
	print("after prediction")
	accuracy = svm_model_linear.score(X_test, y_test)
	print('validation accuracy = ' + str(accuracy))
	print("finished embedding_size " + str(embedding_size))
	return accuracy



if __name__ == '__main__':
	main()
