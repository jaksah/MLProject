from main import *
from makeVocabulary import *
import sys


def printcorrectnessascsv(correct, corrrect_clf, total, dataAmount, vocsize):
	hybridCorr = correct
	hybridHitRate = (1.0 * correct) / total
	bernouCorr = corrrect_clf[0]
	bernouHitRate = (1.0 * corrrect_clf[0]) / total
	multiCorr = corrrect_clf[1]
	multiHitRate = (1.0 * corrrect_clf[1]) / total
	randFoCorr = corrrect_clf[2]
	randFoHitRate = (1.0 * corrrect_clf[2]) / total
	svmCorr = corrrect_clf[3]
	svmHitRate = (1.0 * corrrect_clf[3]) / total

	print("%2.2f,%d,%d,%d,%d,%d,%d,%d,%1.4f,%1.4f,%1.4f,%1.4f,%1.4f" % (dataAmount, vocsize, total, bernouCorr, multiCorr, randFoCorr, svmCorr, hybridCorr, bernouHitRate, multiHitRate, randFoHitRate, svmHitRate, hybridHitRate))


def hitratevsdata(classifier, datatype, pruned, dataAmount):

	clfs = getClassifier(classifier)

	testdata, testtarget, traindata, traintarget = selecttrainandtestdata(datatype, pruned)
	vocsize = len(testdata[0])
	predict = [[0 for x in xrange(len(testdata))] for x in xrange(len(clfs))]
	total = len(testdata)

	# Predict for all classifiers
	predictforclassifiers(clfs, predict, testdata, traindata, traintarget)
	# Check correctness
	utargets, winner = checkcorrectness(clfs, predict, testdata, testtarget)
	# CALCULATING CORRECT, WRONG-SIMILARITIES AND CONFUSION MATRIX

	# Calculate correctness and print
	correct, corrrect_clf = calculatecorrectness(clfs, predict, testtarget, winner)
	# Calculate how similar they vote wrong
	# similar_wrong, total_both_wrong = missclassifysimilarity(clfs, predict, testtarget)
	# printsimilarities(classifier, clfs, similar_wrong, total_both_wrong)

	# makeconfusionmatrix(correct, testtarget, total, utargets, winner)

	# END OF CALCULATING CORRECT, WRONG-SIMILARITIES AND CONFUSION MATRIX
	printcorrectnessascsv(correct, corrrect_clf, total, dataAmount, vocsize)
	# printcorrectness(clfs, correct, corrrect_clf, total)
	# pl.show()


if __name__ == '__main__':
	if (len(sys.argv) == 5):
		clf = sys.argv[1]
		datatype = sys.argv[2]
		pruned = sys.argv[3]
		dataAmount = sys.argv[4]
	hitratevsdata(clf, datatype, int(pruned), float(dataAmount))