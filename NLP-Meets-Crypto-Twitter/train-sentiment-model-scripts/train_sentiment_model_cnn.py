import io
import sys
import csv
import numpy as np
import pandas as pd

from gensim.models import Word2Vec
from gensim.models import KeyedVectors

from sklearn.svm import SVC

from string import punctuation
from os import listdir
from numpy import array
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Flatten
from keras.layers import Embedding
from keras.layers.convolutional import Conv1D
from keras.layers.convolutional import MaxPooling1D

def main():
	embedding_sizes = [50, 100, 150, 200, 250, 300, 350, 450, 500]

	accuracies = []
	for embedding_size in embedding_sizes:
		acc = train_model(embedding_size)
		accuracies.append(acc)
	print(accuracies)

# helper functions

def gen_labels(df):
	y = []
	for i in range(len(df)):
		label = [0] * 2
		label[int(df.iloc[i]['label']) - 1] = 1
		y.append(label)
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

def normalize(X):
	norm = np.linalg.norm(X)
	X = X/norm
	return X

def train_model(embedding_size):
	wv = Word2Vec.load('embedding_models/word2vec_' + str(embedding_size)+ '.model').wv

	print("starting embedding_size " + str(embedding_size))
	print("before gen_input")
	df = pd.read_csv('twitter-data/combined_tweets.csv')
	X = gen_input(wv, df, embedding_size)
	X = normalize(X)
	X_train = X[:304]
	X_test = X[304:len(df) - 14]
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
	print("before training cnn")
	model = Sequential()
	model.add(Embedding(1, embedding_size, input_length=embedding_size))
	model.add(Conv1D(filters=32, kernel_size=8, activation='relu'))
	model.add(MaxPooling1D(pool_size=2))
	model.add(Flatten())
	model.add(Dense(2, activation='softmax'))
	print(model.summary())

	model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
	model.fit(X_train, y_train, epochs=50, verbose=2)
	print("after training cnn")

	# prediction code
	print("before prediction")
	loss, acc = model.evaluate(X_test, y_test, verbose=0)
	print('Test Accuracy: %f' % (acc*100))
	print("after prediction")
	print("finished embedding_size " + str(embedding_size))
	return acc



if __name__ == '__main__':
	main()
