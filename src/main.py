from sklearn.naive_bayes import BernoulliNB
from sklearn.ensemble import RandomForestClassifier
from sklearn import svm
from jsonToBinary import readWholeFileBernoulli
import glob
import re

def make_train_data():
	traindata = []
	traintarget = []
	for f in glob.glob("../res/articles/training_data/*-articles.json"):
		target = f.replace("-articles.json", "")
		target = re.sub(r".*\/+","",target)
		output = readWholeFileBernoulli(f, target)
		traindata.extend(output[0])
		traintarget.extend(output[1])
	return (traindata, traintarget)
# end make_train_data

def make_test_data():
	testdata = []
	testtarget = []
	for f in glob.glob("../res/articles/test_data/*-articles.json"):
		target = f.replace("-articles.json", "")
		target = re.sub(r".*\/+","",target)
		output = readWholeFileBernoulli(f, target)
		testdata.extend(output[0])
		testtarget.extend(output[1])
	return (testdata, testtarget)
# end make_test_data

def bernoulli_classify():
	clf = BernoulliNB()
	train = make_train_data()
	traindata = train[0]
	traintarget = train[1]

	test = make_test_data()
	testdata = test[0]
	testtarget = test[1]

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
# end bernoulli_classify

def svm_classify():
	clf = svm.LinearSVC();
	train = make_train_data()
	traindata = train[0]
	traintarget = train[1]

	test = make_test_data()
	testdata = test[0]
	testtarget = test[1]

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
# end svm_classify

def random_forest_classify():
	clf = RandomForestClassifier(n_estimators=100);
	train = make_train_data()
	traindata = train[0]
	traintarget = train[1]

	test = make_test_data()
	testdata = test[0]
	testtarget = test[1]

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
# end random_forest_classify


def main():
	random_forest_classify();
	#svm_classify();
	#bernoulli_classify()

# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
	main()
