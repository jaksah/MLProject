import re
from sets import Set
from stemming.porter2 import stem


# Convert article to set that is compatible with vocabulary
def articleToSet(article):
	article = article.split()
	article = Set(article)  # Remove duplicates before cleaning
	article = [x.lower() for x in article]
	article = [re.sub(r"[^a-z-]","",x) for x in article]
	article = [re.sub(r"--+","",x) for x in article]
	article = [re.sub(r"^-","",x) for x in article]
	article = [stemword(x) for x in article]
	articleset = Set(article)  # Remove duplicates after stemming
	return articleset
# end def


def stemword(aword):
	return stem(aword)