import json
import tokenize
import re
import numpy
import pickle
from sets import Set

def makeBinaryArrayBernoulli(j):
	with open('vocabularyList', 'rb') as f:
		my_list = pickle.load(f)
	output = [0]*len(my_list)

	articleSet = j['article'].split( )
	articleSet = [x.lower() for x in articleSet] # To lower case
	articleSet = [re.sub(r"[^a-z-]","",x) for x in articleSet]
	articleSet = [re.sub(r"--+","",x) for x in articleSet]
	articleSet = [re.sub(r"^-","",x) for x in articleSet]
	for i in range(len(my_list)):
		if my_list[i] in articleSet:
			output[i] = 1
		#end if
	#end for
	return output
#end of function

def readWholeFileBernoulli(filename,target):
	fil = open(filename)
	j = json.load(fil)
	fil.close()
	total = []
	for article in j:
		o = makeBinaryArrayBernoulli(article)
		total.append(o)
	#end for
	t = [target]*len(total)
	return total, t
#end of function

# def main():
# 	fname = 'sports-articles.json'
# 	target = fname.replace("-articles.json", "")
# 	o = readWholeFileBernoulli(fname,target)
# 	s = o[0]
# 	t = o[1]
# 	print len(t)
# 	print len(o)

# Standard boilerplate to call the main() function to begin
# the program.
# if __name__ == '__main__':
# 	main()
