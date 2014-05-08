from sklearn.naive_bayes import BernoulliNB
import numpy as np
X = np.random.randint(2, size=(6,100))
Y = np.array([1, 2, 3, 4, 4, 5])
print X
print Y
clf = BernoulliNB()
clf.fit(X,Y)
print(clf.predict(X[2]))