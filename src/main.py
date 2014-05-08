from sklearn.naive_bayes import BernoulliNB
from jsonToBinary import readWholeFileBernoulli
import glob


def bernoulli_classify():
	clf = BernoulliNB()
	traindata = []
	traintarget = []
	for f in glob.glob("../res/articles/training_data/*-articles.json"):
		target = f.replace("-article.json", "")
		output = readWholeFileBernoulli(f,target)
		traindata.append(output[0])
		traintarget.append(output[1])

	testdata = []
	testtarget = []
	for f in glob.glob("../res/articles/test_data/*-articles.json"):
		target = f.replace("-article.json", "")
		output = readWholeFileBernoulli(f,target)
		testdata.append(output[0])
		testtarget.append(output[1])

	clf.fit(traindata, traintarget)
	ncorrect = 0
	total = len(testdata)
	for i in range(len(testdata)):
		predict = clf.predict(testdata[i])
		correct = testtarget[i]
		if predict == correct:
			total += 1

		print("Correct: {0} - Predicted: {1}".format(correct, predict))

	print "Correctness", ncorrect/total


def main():
	bernoulli_classify()

# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
	main()