import json
import random as rand
import os
import errno
from os import listdir


def dividetotrainandtestsets():
	parentdir = os.path.abspath(os.path.join(__file__, os.pardir))  # sandbox
	parentdir = os.path.abspath(os.path.join(parentdir, os.pardir))  # src
	parentdir = os.path.abspath(os.path.join(parentdir, os.pardir))  # MLProject
	parentdir = os.path.abspath(os.path.join(parentdir, os.pardir))  # MLProject
	jsondir = parentdir + '/res/articles/'

	articlefiles = []
	fileending = "-articles.json"
	for fileName in listdir(jsondir):
		if fileName.endswith(fileending):
			articlefiles.append(fileName)
		#endif
	#endfor

	chancetotest = 0.33

	for fileName in articlefiles:
		testarticles = []
		trainarticles = []
		# Open JSON file
		json_data = open(jsondir + fileName)
		data = json.load(json_data)
		json_data.close()
		for artObj in data:
			# artObj["article"] = filter(lambda x: x in string.printable, artObj["article"])
			# artObj["title"] = filter(lambda x: x in string.printable, artObj["title"])
			if rand.random() < chancetotest:
				testarticles.append(artObj)
			else:
				trainarticles.append(artObj)
			#endif
		#endfor

		with open(jsondir + 'training_data/' + fileName, 'w') as trainf:
			json.dump(trainarticles, trainf, indent=4, sort_keys=True)
		#endwith 

		with open(jsondir + 'test_data/' + fileName, 'w') as testf:
			json.dump(testarticles, testf, indent=4, sort_keys=True)
		#endwith
		#endfor


def silentremove(filename):
	try:
		os.remove(filename)
	except OSError as e:
		if e.errno != errno.ENOENT:  # errno.ENOENT = no such file or directory
			raise  # re-raise exception if a different error occure


def main():
	dividetotrainandtestsets()

# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
	main()

