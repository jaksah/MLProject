import json
import os.path
import string
import random as rand
import os, errno
from os import listdir

def divideToTrainAndTestSets():
	parentDir = os.path.abspath(os.path.join(__file__, os.pardir)) 	# sandbox
	parentDir = os.path.abspath(os.path.join(parentDir, os.pardir)) # src
	parentDir = os.path.abspath(os.path.join(parentDir, os.pardir)) # MLProject
	parentDir = os.path.abspath(os.path.join(parentDir, os.pardir)) # MLProject
	jsonDir = parentDir + '/res/articles/'

	articleFiles = []
	fileEnding = "-articles.json"
	for fileName in listdir(jsonDir):
		if fileName.endswith(fileEnding):
			articleFiles.append(fileName)
		#endif
	#endfor


	chanceToTest = 0.33
	ctr = 0

	for fileName in articleFiles:
		testArticles = []
		trainArticles = []
		# Open JSON file
		json_data = open(jsonDir + fileName)
		data = json.load(json_data)
		json_data.close()
		for artObj in data:
			# artObj["article"] = filter(lambda x: x in string.printable, artObj["article"])
			# artObj["title"] = filter(lambda x: x in string.printable, artObj["title"])
			if rand.random() < chanceToTest:
				testArticles.append(artObj)
			else:
				trainArticles.append(artObj)
			#endif
		#endfor

		with open(jsonDir + 'training_data/'+fileName, 'w') as trainf:
			json.dump(trainArticles, trainf,indent=4, sort_keys=True)
			# print json.dumps(trainArticles, indent=4, sort_keys=True)
		#endwith 

		with open(jsonDir + 'test_data/'+fileName, 'w') as testf:
			json.dump(testArticles, testf,indent=4, sort_keys=True)
			# print json.dumps(testArticles, indent=4, sort_keys=True)
		#endwith 
	#endfor

def silentremove(filename):
	try:
		os.remove(filename)
	except OSError as e:
		if e.errno != errno.ENOENT: # errno.ENOENT = no such file or directory
			raise # re-raise exception if a different error occure

def main():
	divideToTrainAndTestSets()

# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
	main()

