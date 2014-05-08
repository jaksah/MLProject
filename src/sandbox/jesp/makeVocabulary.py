import json
import tokenize
import glob
import os
import re
import pickle
from sets import Set

vocabularySet = Set()

for f in glob.glob("../../../crawler/news/*-articles.json"):
	jsonFile = json.load(open(f))
	for line in jsonFile:
		article = line['article'].split( )
		article = [x.lower() for x in article]
		article = [re.sub(r"[^a-z-]","",x) for x in article]
		article = [re.sub(r"--+","",x) for x in article]
		article = [re.sub(r"^-","",x) for x in article]
		articleSet = Set(article)
		vocabularySet = vocabularySet | articleSet
	# end for
# end for

vocabulary = sorted(list(vocabularySet))

with open('vocabularyList', 'wb') as f:
	pickle.dump(vocabulary, f)
	f.close()