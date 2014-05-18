import tokenize
import re
from sets import Set

# Convert article to set that is compatible with vocabulary
def articleToSet(article):
	article = article.split( )
	article = [x.lower() for x in article]
	article = [re.sub(r"[^a-z-]","",x) for x in article]
	article = [re.sub(r"--+","",x) for x in article]
	article = [re.sub(r"^-","",x) for x in article]
	articleSet = Set(article)
	return articleSet
# end def