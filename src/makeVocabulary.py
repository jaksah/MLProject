import json
import glob
import pickle
import numpy
import sys
from common import *
from jsonToBinary import *
from sklearn.feature_selection import SelectKBest, chi2


def makeVocabulary(dataAmount):
	vocabularySet = set()

	counter = 0
	d = 1/dataAmount
	for f in glob.glob("../res/articles/training_data/*-articles.json"):
		jsonFile = json.load(open(f))
		for line in jsonFile:
			if (int(counter%d) == 0):
				articleSet = articleToSet(line['article'])
				vocabularySet = vocabularySet | articleSet
			counter+=1
		# end for
	# end for

	vocabulary = sorted(list(vocabularySet))

	with open('vocabularyList', 'wb') as f:
		pickle.dump(vocabulary, f)
		f.close()

	training_data = make_data('training',0)
	targets = training_data[0]
	samples = training_data[2]
	feature_selector = SelectKBest(chi2,500)
	selected_samples = feature_selector.fit(samples,targets).get_support()

	pruned_vocabulary = []
	for i in range(0,len(selected_samples)):
		if selected_samples[i]:
			pruned_vocabulary.append(vocabulary[i])

	with open('prunedVocabularyList', 'wb') as f:
		pickle.dump(pruned_vocabulary, f)
		f.close()

if __name__ == '__main__':
	if (len(sys.argv) == 2):
		dataAmount = sys.argv[1]
		makeVocabulary(float(dataAmount))