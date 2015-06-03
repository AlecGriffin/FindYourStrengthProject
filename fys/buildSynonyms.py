import urllib2,sqlite3,json

baseUrlPrefix = "http://www.thesaurus.com/browse/"
baseUrlSuffix = "?s=t"

def getSyn(word):
    pass
def initDB(bibleSet):
    conn = sqlite3.connect("synon.db")
    c = conn.cursor()
    c.execute('CREATE TABLE {tn} ({nf} {ft} PRIMARY KEY)'.format(tn="syn",nf='synon',ft='TEXT'))

if __name__=="__main__":
	f = open("bible.txt")
	bibleList = list(set(f))
	#print bibleList[1]
	bibleSet = set()
	for i in bibleList:
		mylist = (i.split("	")[1]).split()
		bibleSet |=set(mylist)
	print len(bibleSet)