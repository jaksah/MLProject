import json
import pickle
import glob
import re
import numpy as np
from common import *
from sklearn.preprocessing import Normalizer


def make_data(type,pruned):
	databinary = []
	target = []
	datacount = []
	data_l2 = []
	data_mapped = []
	for f in glob.glob("../res/articles/" + type + "_data/*-articles.json"):
		t = f.replace("-articles.json", "")
		t = re.sub(r".*\/+","",t)
		o = readWholeFileBernoulli(f,t,pruned)
		
		target.extend(o[0])
		datacount.extend(o[2])

		databinary.extend(o[1])
		data_l2.extend(o[3])
		data_mapped.extend(o[4])
	return (target, databinary, datacount , data_l2, data_mapped)
# end make_data

def makeCountArray(j,pruned):
	voc = 'vocabularyList'
	if pruned == 1:
		voc = 'prunedVocabularyList'
	with open(voc, 'rb') as f:
		vocab = pickle.load(f)
	output = [0]*len(vocab)

	article = articleToList(j['article'])
	doclen = len(article)
	for i in range(doclen):
		if article[i] in vocab:
			output[vocab.index(article[i])] += 1
		#end if
	#end for
	return output
#end of function

def readWholeFileBernoulli(filename,target,pruned):
	fil = open(filename)
	j = json.load(fil)
	fil.close()
	total = []
	totalbinary = []
	data_l2 = []
	data_mapped = []

	norm = Normalizer(norm='l2')

	eps = 0.0000001  # To avoid division by 0

	for article in j:
		if not article['article']:
			continue
		o = makeCountArray(article,pruned)

		# Count array
		total.append(o)


		# Binary array
		obin = [1 if x>0 else 0 for x in o]
		totalbinary.append(obin)

		# L2 norm
		data_float = [float(x) for x in o]
		data_float = norm.transform([data_float]).tolist()[0]
		data_l2.append(data_float)

		# Mapped
		imaxim = 1/(max(o)+eps)
		data_float = [x*imaxim for x in o]
		data_mapped.append(data_float)

	#end for
	t = [target]*len(total)
	return t, totalbinary, total, data_l2, data_mapped
#end of function

