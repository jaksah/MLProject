from sklearn.naive_bayes import BernoulliNB, MultinomialNB
from sklearn.ensemble import RandomForestClassifier
from sklearn import svm
from jsonToBinary import *
import sys


def getClassifier(x):

	clf = {
		'ber': [BernoulliNB()],
		'mn': [MultinomialNB()],
		'rf': [RandomForestClassifier(n_estimators=500)],
		'svm': [svm.SVC(kernel='linear')],
		'hybrid': [BernoulliNB(), MultinomialNB(), RandomForestClassifier(n_estimators=500), svm.SVC(kernel='linear')]
		}.get(x, [MultinomialNB()])
	return clf


def hasuniquemax(targetcount):
	sortcount = sorted(targetcount, reverse=True)
	return sortcount[0] != sortcount[1]



def classify(classifier, datatype, pruned):
	clfs = getClassifier(classifier)
	print clfs

	train = make_data('training',pruned)
	traintarget = train[0]
	traindata = train[int(datatype)]

	test = make_data('test',pruned)
	testtarget = test[0]
	testdata = test[int(datatype)]
	ncorrect = [0]*len(clfs)
	predict = [[0 for x in xrange(len(testdata))] for x in xrange(len(clfs))]
	total = len(testdata)

	# Predict for all classifiers
	for c in range(0,len(clfs)):
		clf = clfs[c]
		clf.fit(traindata, traintarget)
		for i in range(len(testdata)):
			predict[c][i] = clf.predict(testdata[i])

	# Check correctness
	utargets = list(set(testtarget))
	ntargets = len(utargets)
	winner = [0]*len(testtarget)
	for i in range(len(testdata)):
		targetcount = [0]*ntargets
		for c in range(len(clfs)):
			classpredicted = predict[c][i]
			targetcount[utargets.index(classpredicted)]+=1
		winidx = -1
		if hasuniquemax(targetcount):
			winidx = targetcount.index(max(targetcount))
		else:
			winidx = utargets.index(predict[1][i])  # Set default clf winner
		winner[i] = utargets[winidx]

	correct = 0
	for i in range(len(testtarget)):

		if testtarget[i] == winner[i]:
			correct += 1

	print("Correct: {0} - Total: {1} - Correctness: {2}".format(correct, total, (1.0*correct)/total))
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
		print("hybrid: Hybrid of all")
		clf = raw_input("Choose classifier: ")

		print(" ")
		print("Datatypes:")
		print("1: Binary array")
		print("2: Count array")
		print("3: Count normalized by document size")
		print("4: Count normalized by max(countsArray)")
		datatype = raw_input("Choose datatype: ")
		print(" ")
		pruned = int(raw_input("Pruned vocabulary (1 or 0): "))

	classify(clf, datatype, pruned)

# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
	main()