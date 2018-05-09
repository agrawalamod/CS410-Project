import csv
import sys
import numpy as np
import time
from collections import Counter
import os
import nltk
from math import log
import operator
import glob
import os.path, time
import csv
import numpy as np
import time
from collections import Counter
import glob
import os.path, time
import json
import re
from nltk.tokenize import RegexpTokenizer
from nltk.stem.porter import *
from nltk.corpus import stopwords
from scipy import spatial
from nltk.tag import StanfordNERTagger
from math import *
import ast

stemmer = PorterStemmer()
tokenizer = RegexpTokenizer(r'\w+')

inverted_index = {}
f = open('inverted_index.csv')
csv_f = csv.reader(f)
for row in csv_f:
	inverted_index[row[0]] = ast.literal_eval(row[1])


print inverted_index
query = raw_input()

def pre_process(doc):

	doc = doc.replace('"', '')
	tokens = tokenizer.tokenize(doc)
	stemmed_doc = []
	for word in tokens:
		if word not in stopwords.words('english'):
			try:
				stemmed_doc.append(stemmer.stem(word))
			except Exception, e:
				print e
				stemmed_doc.append(word)

	return stemmed_doc

stemmed_query = pre_process(query)


rel_docs = {}

for query_word in stemmed_query:
	if query_word in inverted_index:
		docs = inverted_index[query_word]
		print docs
		for doc in docs:
			if doc[0] not in rel_docs.keys():
				rel_docs[doc[0]] = []
				t_doc = rel_docs[doc[0]]
				t_doc.append(doc[1])
				rel_docs[doc[0]] = t_doc
			else:
				t_doc = rel_docs[doc[0]]
				t_doc.append(doc[1])
				rel_docs[doc[0]] = t_doc

print rel_docs




