import json
import pickle
import glob
import re
from common import *


def make_data(type,pruned):
	databinary = []
	target = []
	datacount = []
	data_doclen_norm = []
	data_count_norm = []
	for f in glob.glob("../res/articles/" + type + "_data/*-articles.json"):
		t = f.replace("-articles.json", "")
		t = re.sub(r".*\/+","",t)
		o = readWholeFileBernoulli(f,t,pruned)
		
		target.extend(o[0])
		databinary.extend(o[1])
		datacount.extend(o[2])
		data_doclen_norm.extend(o[3])
		data_count_norm.extend(o[4])
	return (target, databinary, datacount, data_doclen_norm, data_count_norm)
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
	return output, 1.0/doclen
#end of function

def readWholeFileBernoulli(filename,target,pruned):
	fil = open(filename)
	j = json.load(fil)
	fil.close()
	total = []
	totalbinary = []
	total_doclen_norm = []
	total_count_norm = []
	for article in j:
		if not article['article']:
			continue
		(o,inv_doclen) = makeCountArray(article,pruned)
		total.append(o)
		
		o_temp = [x*inv_doclen for x in o]
		total_doclen_norm.append(o_temp)
		
		inv_osum = 1.0/sum(o)
		o_temp = [x*inv_osum for x in o]
		total_count_norm.append(o_temp)
		
		obin = [1 if x>0 else 0 for x in o]
		totalbinary.append(obin)
	#end for
	t = [target]*len(total)
	return t, totalbinary, total, total_doclen_norm, total_count_norm
#end of function
