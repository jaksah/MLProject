import json
import tokenize
import glob
import os
import re
import pickle
from common import *
from sets import Set
vocabularySet = Set()

for f in glob.glob("../../../res/articles/training_data/*-articles.json"):
	jsonFile = json.load(open(f))
	for line in jsonFile:
		articleSet = articleToSet(line['article']);
		vocabularySet = vocabularySet | articleSet
	# end for
# end for

vocabulary = sorted(list(vocabularySet))

for word in vocabulary:
	print word
# end for

#with open('vocabularyList', 'wb') as f:
#	pickle.dump(vocabulary, f)
#	f.close()