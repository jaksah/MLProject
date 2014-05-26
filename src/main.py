from sklearn.naive_bayes import BernoulliNB, MultinomialNB
from sklearn.ensemble import RandomForestClassifier
from sklearn import svm
from jsonToBinary import *
import sys
import pylab as pl
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
from collections import Counter


def getClassifier(x):

	clf = {
		'ber': [BernoulliNB()],
		'mn': [MultinomialNB()],
		'rf': [RandomForestClassifier(n_estimators=500)],
		'svm': [svm.SVC(kernel='linear')],
		'hybrid': [BernoulliNB(), MultinomialNB(), RandomForestClassifier(n_estimators=500), svm.SVC(kernel='linear')]
		}.get(x, [MultinomialNB()])
	return clf

def getClassifierName(x):

	clf = {
		'ber': ['Bernou'],
		'mn':  ['Multin'],
		'rf':  ['RandFo'],
		'svm': ['SuppVM'],
		'hybrid': ['Bernou','Multin','RandFo','SuppVM']
		}.get(x, ['Multin'])
	return clf


def hasuniquemax(targetcount):
	sortcount = sorted(targetcount, reverse=True)
	return sortcount[0] != sortcount[1]

def printSimilarityWrong(clfs, testtarget, predict, classifier):
	clfcomb = 0
	for i in range(len(clfs)):
		clfcomb += i # Number of clf-combinations
	total_both_wrong = [0]*clfcomb
	similar_wrong = [0]*clfcomb
	for i in range(len(testtarget)):
		tmp_index = 0
		for j in range(len(clfs)-1):
			for k in range(j+1,len(clfs)):
				if(predict[j][i] != testtarget[i] and predict[k][i] != testtarget[i]):
					total_both_wrong[tmp_index] +=1
				if (predict[j][i] != testtarget[i] or predict[k][i] != testtarget[i]) and predict[k][i] == predict[j][i]:
					similar_wrong[tmp_index] +=1
				tmp_index += 1

	print("Similarities:")
	tmp_index = 0
	names = getClassifierName(classifier)
	for i in range(len(clfs)-1):
		for j in range(i+1,len(clfs)):
			print("{0} for {1} - {2}".format((100.0*similar_wrong[tmp_index])/total_both_wrong[tmp_index],names[i],names[j]))
			tmp_index += 1

def plotConfusionMatrix(clfs,testtarget,winner,correct,total,utargets):
	cm_count = confusion_matrix(testtarget, winner)
	cm = cm_count
	#cm = cm / cm.astype(np.float).sum(axis=1) # Normalized count for percentage
	cm = [(1.0*x)/x.sum(axis=0) for x in cm]

	# Add one more column and row with zeros and a "total" at diagonal
	cm = np.append(cm,[[1] for x in xrange(len(cm))],1)
	last_row = [0 for x in xrange(len(cm))]
	last_row.append((1.0*correct)/total) # Percentage correct in right, down corner
	cm = np.append(cm,[last_row],0)

	cm_count = np.append(cm_count,[[x] for x in cm_count.sum(axis=1)],1)
	last_row = [0 for x in xrange(len(cm_count))]
	last_row.append(correct) # Total correct in right, down corner
	cm_count = np.append(cm_count,[last_row],0)

	# Show confusion matrix in a separate window
	cax = pl.matshow(cm)
	# Set count and percentage labels in plot
	for j in xrange(len(cm)): 
		for i in xrange(len(cm[0])):
			pl.annotate("%d\n(%2.1f%%)" %(cm_count[j][i],100*cm[j][i]),xy=(i-1.0/2.5,j+1.0/7))
	
	# Add the Total-label
	utargets.append('Total')

	#pl.title('Confusion matrix')
	pl.colorbar(cax)
	pl.ylabel('True label')
	pl.xlabel('Predicted label')
	pl.xticks(np.arange(len(utargets)),utargets,rotation=70)
	pl.yticks(np.arange(len(utargets)),utargets)
	pl.show()

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
	utargets = sorted(list(set(testtarget)))
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


	# Calculate correctness and print
	correct = 0
	corrrect_clf = [0]*len(clfs)
	for i in range(len(testtarget)):
		if testtarget[i] == winner[i]:
			correct += 1
		for j in range(len(clfs)):
			if testtarget[i] == predict[j][i]:
				corrrect_clf[j] += 1

	# Calculate how similar they vote wrong
	printSimilarityWrong(clfs, testtarget, predict, classifier)

	print("Correct: {0} - Total: {1} - Correctness: {2}".format(correct, total, (1.0*correct)/total))
	if len(clfs) == 4:
		print("Bernou -- Correct: {0} - Total: {1} - Correctness: {2}".format(corrrect_clf[0], total, (1.0*corrrect_clf[0])/total))
		print("Multin -- Correct: {0} - Total: {1} - Correctness: {2}".format(corrrect_clf[1], total, (1.0*corrrect_clf[1])/total))
		print("RandFo -- Correct: {0} - Total: {1} - Correctness: {2}".format(corrrect_clf[2], total, (1.0*corrrect_clf[2])/total))
		print("SuppVM -- Correct: {0} - Total: {1} - Correctness: {2}".format(corrrect_clf[3], total, (1.0*corrrect_clf[3])/total))

	# Plot a confusion matrix
	plotConfusionMatrix(clfs,testtarget,winner,correct,total,utargets)

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
		print("3: L2-normalized count array")
		print("4: Count array mapped from 0 to 1")
		datatype = raw_input("Choose datatype: ")
		print(" ")
		pruned = int(raw_input("Pruned vocabulary (1 or 0): "))

	classify(clf, datatype, pruned)

# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
	main()