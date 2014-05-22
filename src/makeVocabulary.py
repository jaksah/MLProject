import json
import glob
import pickle
from sets import Set
from common import *

vocabularySet = Set()

for f in glob.glob("../res/articles/training_data/*-articles.json"):
	jsonFile = json.load(open(f))
	for line in jsonFile:
		articleSet = articleToSet(line['article'])
		vocabularySet = vocabularySet | articleSet
	# end for
# end for

vocabulary = sorted(list(vocabularySet))

with open('vocabularyList', 'wb') as f:
	pickle.dump(vocabulary, f)
	f.close()