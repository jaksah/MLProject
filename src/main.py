from sklearn.naive_bayes import BernoulliNB, MultinomialNB
from sklearn.ensemble import RandomForestClassifier
from sklearn import svm
from jsonToBinary import *
import sys


def getClassifier(x):
	clf = {
		'ber': BernoulliNB(),
		'mn': MultinomialNB(),
		'rf': RandomForestClassifier(n_estimators=500),
		'svm': svm.SVC(kernel='linear'),
		}.get(x, svm.SVC(kernel='linear'))
	return clf


def classify(classifier, datatype, pruned):
	clf = getClassifier(classifier)
	print clf
	train = make_data('training',pruned)
	traintarget  = train[0]
	traindata = train[int(datatype)]

	test = make_data('test',pruned)
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
	if (len(sys.argv) == 3):
		clf = sys.argv[1]
		datatype = sys.argv[2]
	else:
		print("Classifiers:")
		print("ber: Bernoulli")
		print("mn: Multinomial")
		print("rf: Random Forest")
		print("svm: SVM")
		clf = raw_input("Choose classifier: ")

		print(" ")
		print("Datatypes:")
		print("1: Binary array")
		print("2: Count array")
		print("3: Count normalized by document size")
		print("4: Count normalized by sum(countsArray)")
		datatype = raw_input("Choose datatype: ")
		pruned = int(raw_input("Pruned vocabulary (1 or 0): "))

	classify(clf, datatype, pruned)

# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
	main()