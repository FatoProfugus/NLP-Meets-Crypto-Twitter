import io
import sys
import csv
import numpy as np
import pandas as pd

from gensim.models import Word2Vec
from gensim.models import KeyedVectors

from sklearn.svm import SVC

def main():
	embedding_sizes = [50, 100]
	df = pd.read_csv('btc_keyword_corpus_2021.csv')
	tweets = gen_sentences(list(df.iloc[:]['Tweets']))
	
	print("embedding_model training started")
	for i in range(len(embedding_sizes)):
		embedding_size = embedding_sizes[i]
		embedding_model = Word2Vec(sentences=tweets, vector_size=embedding_size,
			window=5, min_count=1, workers=4)
		embedding_model.save('2021_word2vec_btc_keyword_' + str(embedding_size) + '.model')
		print("embedding_model size " + str(embedding_size) + " training finished")
	print("embedding_model training finished")

def gen_sentences(tweets):
	sentence = []
	sentences = []
	for i in range(len(tweets)):
		words = tweets[i]
		if (pd.isna(words)):
				continue
		sentence += words.split()
		sentences.append(sentence)
		sentence = []
	return sentences

if __name__ == '__main__':
	main()