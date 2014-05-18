from sklearn.naive_bayes import BernoulliNB
from sklearn import svm
from jsonToBinary import readWholeFileBernoulli
import glob
import re


def bernoulli_classify():
	clf = BernoulliNB()
	traindata = []
	traintarget = []
	for f in glob.glob("../res/articles/training_data/*-articles.json"):
		target = f.replace("-articles.json", "")
		target = re.sub(r".*\/+","",target)
		output = readWholeFileBernoulli(f, target)
		traindata.extend(output[0])
		traintarget.extend(output[1])

	testdata = []
	testtarget = []
	for f in glob.glob("../res/articles/test_data/*-articles.json"):
		target = f.replace("-articles.json", "")
		target = re.sub(r".*\/+","",target)
		output = readWholeFileBernoulli(f, target)
		testdata.extend(output[0])
		testtarget.extend(output[1])

	clf.fit(traindata, traintarget)
	ncorrect = 0
	total = len(testdata)
	for i in range(len(testdata)):
		predict = clf.predict(testdata[i])
		correct = testtarget[i]
		if correct == predict[0]:
			ncorrect += 1

		print("Correct: {0} - Predicted: {1}".format(correct, predict[0]))

	print "Correct ", ncorrect, " Total ", total, " Correctness ", ncorrect*1.0/total

def svm_classify():
	clf = svm.LinearSVC();
	traindata = []
	traintarget = []
	for f in glob.glob("../res/articles/training_data/*-articles.json"):
		target = f.replace("-articles.json", "")
		target = re.sub(r".*\/+","",target)
		output = readWholeFileBernoulli(f, target)
		traindata.extend(output[0])
		traintarget.extend(output[1])

	testdata = []
	testtarget = []
	for f in glob.glob("../res/articles/test_data/*-articles.json"):
		target = f.replace("-articles.json", "")
		target = re.sub(r".*\/+","",target)
		output = readWholeFileBernoulli(f, target)
		testdata.extend(output[0])
		testtarget.extend(output[1])

	clf.fit(traindata, traintarget)
	ncorrect = 0
	total = len(testdata)
	for i in range(len(testdata)):
		predict = clf.predict(testdata[i])
		correct = testtarget[i]
		if correct == predict[0]:
			ncorrect += 1

		print("Correct: {0} - Predicted: {1}".format(correct, predict[0]))

	print "Correct ", ncorrect, " Total ", total, " Correctness ", ncorrect*1.0/total


def main():
	svm_classify();
	#bernoulli_classify()

# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
	main()
