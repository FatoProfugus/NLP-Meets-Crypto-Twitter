import io
import sys
import csv
import numpy as np
import pandas as pd

from gensim.models import Word2Vec
from gensim.models import KeyedVectors

from sklearn.svm import SVC

import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from keras.models import Sequential
from keras.layers import LSTM
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import Flatten
from keras import optimizers
import sys

"""
num_layers = [2, 3, 3, 5, 5,
              4, 5, 4, 5, 6,
              5, 5, 7, 5, 5]

drop = [[0.37, 0.55, 0.00, 0.00, 0.00, 0.00, 0.00],
        [0.22, 0.22, 0.50, 0.00, 0.00, 0.00, 0.00],
        [0.25, 0.25, 0.60, 0.00, 0.00, 0.00, 0.00],
        [0.30, 0.30, 0.30, 0.25, 0.50, 0.00, 0.00],	
        [0.20, 0.20, 0.20, 0.25, 0.50, 0.00, 0.00],	
        [0.15, 0.15, 0.15, 0.00, 0.00, 0.00, 0.00],
        [0.15, 0.15, 0.15, 0.15, 0.00, 0.00, 0.00],	 
        [0.15, 0.15, 0.15, 0.00, 0.00, 0.00, 0.00],	 
        [0.15, 0.15, 0.15, 0.15, 0.00, 0.00, 0.00],	 
        [0.15, 0.15, 0.15, 0.15, 0.15, 0.00, 0.00],
        [0.10, 0.10, 0.10, 0.10, 0.20, 0.10, 0.10],
        [0.10, 0.10, 0.10, 0.10, 0.20, 0.10, 0.10],
        [0.10, 0.10, 0.10, 0.10, 0.20, 0.10, 0.10],
        [0.10, 0.10, 0.10, 0.10, 0.20, 0.10, 0.10],	  
        [0.10, 0.10, 0.10, 0.10, 0.20, 0.10, 0.10]]

neurons = [[90, 7],
           [60, 50, 40], 
           [65, 50, 50],
           [90, 90, 90, 50, 50],
           [60, 55, 55, 40, 40],
           [50, 50, 50, 50],
           [25, 25, 25, 25, 25],
           [25, 25, 25, 25],
           [50, 50, 50, 50, 50],
           [70, 70, 70, 70, 70, 70],
           [50, 60, 70, 50, 40],
           [50, 60, 70, 50, 40],
           [50, 60, 70, 50, 40, 20, 20],
           [50, 60, 70, 50, 40],
           [50, 60, 70, 50, 40]]
"""
num_layers = [5]
drop = [[0.10, 0.10, 0.10, 0.10, 0.20, 0.10, 0.10]]
neurons = [[50, 60, 70, 50, 40]]

def main():
	train_model()

# helper functions

def gen_labels(df):
	y = []
	for i in range(len(df)):
		label = [0] * 6
		label[int(df.iloc[i]['label']) - 1] = 1
		y.append(label)
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

def train_model():
	df = pd.read_csv('bitcoin_clean_2020_2021.csv')
	df_sent = pd.read_csv('2021_SBF_FTX_sentiment6_svm50.csv')
	df['Sentiment'] = df_sent['sentiment']/7
	labels = pd.read_csv('labels_6.csv')

	df.drop(['Unnamed: 0', 'Date'], axis=1, inplace=True)
	labels.drop(['Unnamed: 0'], axis = 1, inplace=True)

	# Split train test data by . Split training data and validation by .
	labels = gen_labels(labels)
	features_train = df.iloc[366:366+304, :].values
	labels_train = labels[366:366+304, :]
	features_test = df.iloc[366+304:len(df)-14-1, :].values
	labels_test = labels[366+304:len(df)-1, :]

	scaler = StandardScaler()
	scaler = scaler.fit(features_train)

	features_train_scaled = scaler.transform(features_train)
	features_test_scaled = scaler.transform(features_test)

	# Define LSTM step size.
	step_size = 30
	validation_clip = math.floor((0.75)*len(features_train))

	X_train = []
	y_train = []
	for i in range(step_size, validation_clip):
		X_train.append(features_train_scaled[i-step_size:i, :])
		y_train.append(labels_train[i, :])

	X_train, y_train = np.array(X_train), np.array(y_train)
	#y_train = np.reshape(y_train, (y_train.shape[0], y_train.shape[1], 1))
	
	X_val = []
	y_val = []
	for i in range(validation_clip, len(features_train)):
		X_val.append(features_train_scaled[i-step_size:i, :])
		y_val.append(labels_train[i, :])

	X_val, y_val = np.array(X_val), np.array(y_val)
	#y_val = np.reshape(y_val, (y_val.shape[0], y_val.shape[1], 1))

	X_test = []
	y_test = []
	for i in range(step_size, len(features_test)):
		X_test.append(features_test_scaled[i-step_size:i, :])
		y_test.append(labels_test[i, :])
	
	X_test, y_test = np.array(X_test), np.array(y_test)
	#y_test = np.reshape(y_test, (y_test.shape[0], y_test.shape[1], 1))

	sgd = optimizers.SGD(lr=0.01, clipvalue=1)



	for j in range(1):
		layers = num_layers[j]
		neur   = neurons[j]
		dr     = drop[j]

		regressor = Sequential()

		regressor.add(LSTM(units = neur[0], return_sequences = True,
			input_shape = (X_train.shape[1], X_train.shape[2])))
		regressor.add(Dropout(dr[0]))

		for i in range(1, layers):
			if(i == layers-1):
				regressor.add(LSTM(units = neur[i], return_sequences = False))
			else:
				regressor.add(LSTM(units = neur[i], return_sequences = True))
			regressor.add(Dropout(dr[i]))
		
		regressor.add(Dense(units = 6, activation = 'softmax'))

		regressor.compile(optimizer = 'sgd', loss = 'categorical_crossentropy',
			metrics = ['accuracy'])


		sys.stdout = sys.__stdout__
		history = regressor.fit(X_train, y_train, epochs = 30,
			batch_size = 32, validation_data = (X_val, y_val), shuffle = False)

		train_loss, train_acc = regressor.evaluate(X_train, y_train)
		test_loss, test_acc = regressor.evaluate(X_test, y_test)

		print("train_loss: " + str(train_loss))
		print("train_acc: " + str(train_acc))
		print("test_loss: " + str(test_loss))
		print("test_acc: " + str(test_acc))

		#test_results[ind].append(test_acc)

		#sys.stdout = open(market[ind]+"Results.txt","a")
		#print('Model', j+1, ':', 'Training set accuracy:', train_acc)
		#print('Model', j+1, ':', 'Test set accuracy:', test_acc)
		#print('\n')

		#plt.plot(history.history['acc'], label='train')
		#plt.plot(history.history['val_acc'], label='val')
		#plt.legend()
		#plt.title('Binary Crossentropy: Train vs. Val')
		#plt.xlabel('epoch')
		#plt.ylabel('accuracy')
		#plt.savefig(market[ind]+'Model'+str(j+1)+'.png', bbox_inches='tight')

		regressor = None



if __name__ == '__main__':
	main()
