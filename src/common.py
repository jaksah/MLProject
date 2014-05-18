import re
from sets import Set
from stemming.porter2 import stem
from nltk.corpus import stopwords


# Convert article to set that is compatible with vocabulary
def articleToSet(article):
	article = articleToList(article)
	articleset = Set(article)  # Remove duplicates after stemming
	return articleset
# end def

# Convert article to set that is compatible with vocabulary
def articleToList(article):
	article = fulltextcleanup(article)
	article = article.split()
	article = [x.lower() for x in article]
	article = singlewordcleanup(article)
	article = removestopwords(article)
	article = [stemword(x) for x in article]
	article = filter(lambda a:a !='', article) # Remove ''

	return article
# end def


def fulltextcleanup(article):
	illegal_patterns = [r"Media playback is unsupported on your device\s*Last updated at \d{2}.\d{2} BST",
						r"Last updated at \d{2}:\d{2}", r"Media requires JavaScript to play"]
	for pattern in illegal_patterns:
		article = re.sub(pattern, "", article)
	#end for
	return article


def singlewordcleanup(article):
	illegal_patterns = [r"[^a-z-]", r"--+", r"^-"]
	for pattern in illegal_patterns:
		article = [re.sub(pattern, "", x) for x in article]
	return article


def stemword(aword):
	return stem(aword)


def removestopwords(alist):
	stop = stopwords.words('english')
	return [i for i in alist if i not in stop]