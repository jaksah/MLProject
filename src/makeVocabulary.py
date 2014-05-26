import json
import glob
import pickle
import numpy
from common import *
from jsonToBinary import *
from sklearn.feature_selection import SelectPercentile, chi2

vocabularySet = set()

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

training_data = make_data('training',0)
targets = training_data[0]
samples = training_data[2]
feature_selector = SelectPercentile(chi2,15)
selected_samples = feature_selector.fit(samples,targets).get_support()

pruned_vocabulary = []
for i in range(0,len(selected_samples)):
	if selected_samples[i]:
		pruned_vocabulary.append(vocabulary[i])

for word in pruned_vocabulary:
	print word
print len(pruned_vocabulary)

with open('prunedVocabularyList', 'wb') as f:
	pickle.dump(pruned_vocabulary, f)
	f.close()