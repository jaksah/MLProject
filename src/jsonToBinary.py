import json
import pickle
from common import *

def makeCountArray(j):
	with open('vocabularyList', 'rb') as f:
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

def readWholeFileBernoulli(filename,target):
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
		(o,inv_doclen) = makeCountArray(article)
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
