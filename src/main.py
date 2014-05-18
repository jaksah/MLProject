from sklearn.naive_bayes import BernoulliNB, MultinomialNB
from sklearn.ensemble import RandomForestClassifier
from sklearn import svm
from jsonToBinary import readWholeFileBernoulli
import glob
import re
import sys


def make_data(type):
	databinary = []
	target = []
	datacount = []
	data_doclen_norm = []
	data_count_norm = []
	for f in glob.glob("../res/articles/" + type + "_data/*-articles.json"):
		t = f.replace("-articles.json", "")
		t = re.sub(r".*\/+","",t)
		o = readWholeFileBernoulli(f, t)
		
		target.extend(o[0])
		databinary.extend(o[1])
		datacount.extend(o[2])
		data_doclen_norm.extend(o[3])
		data_count_norm.extend(o[4])
	return (target, databinary, datacount, data_doclen_norm, data_count_norm)
# end make_data


def getClassifier(x):
	clf = {
		'ber': BernoulliNB(),
		'mn': MultinomialNB(),
		'rf': RandomForestClassifier(n_estimators=100),
		'svm': svm.SVC(kernel='linear'),
		}.get(x, svm.SVC(kernel='linear'))
	return clf


def classify(classifier, datatype):
	clf = getClassifier(classifier)
	print clf
	train = make_data('training')
	traintarget  = train[0]
	traindata = train[int(datatype)]

	test = make_data('test')
	testtarget  = test[0]
	testdata = test[int(datatype)]

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
# end classify


def main():
	clf = sys.argv[1]
	datatype = sys.argv[2]
	classify(clf, datatype)

# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
	main()