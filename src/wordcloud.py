import json
import glob
import pickle
import numpy
import math
from common import *
from jsonToBinary import *
from sklearn.feature_selection import SelectPercentile, chi2

with open('vocabularyList', 'rb') as f:
	vocabulary = pickle.load(f)

training_data = make_data('training',0)
targets = training_data[0]
samples = training_data[2]
feature_selector = SelectPercentile(chi2,10)
selected_samples = feature_selector.fit(samples,targets).get_support()
score = feature_selector.scores_

pruned_vocabulary = []
for i in range(0,len(selected_samples)):
	if selected_samples[i]:
		pruned_vocabulary.append(vocabulary[i])

for i in range(0,len(pruned_vocabulary)):
	for j in range(0,int(score[i])):
		print("{0} ".format(pruned_vocabulary[i])),