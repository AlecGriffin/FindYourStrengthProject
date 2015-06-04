import urllib.request,sqlite3,json,string,re

baseUrlPrefix = "http://www.thesaurus.com/browse/"
baseUrlSuffix = "?s=t"

def getSyn(word):
    pass
def insertion(bibleSet):
	for i in bibleSet:
		s = list(bibleSet)[i]
		s = re.sub(r'[^\w\s]','',s)
		synList = getSyn(s)
		

def initDB():
    conn = sqlite3.connect("synon.db")
    c = conn.cursor()
    c.execute('CREATE TABLE {tn} ({nf} {ft} PRIMARY KEY)'.format(tn="syn",nf='words',ft='TEXT'))
    conn.commit()
    conn.close()
if __name__=="__main__":
	f = open("bible.txt")
	bibleList = list(set(f))
	#print bibleList[1]
	bibleSet = set()
	for i in bibleList:
		mylist = (i.split("	")[1]).split()
		bibleSet |= set(mylist)
	#initDB()
	#insertion(bibleSet)
