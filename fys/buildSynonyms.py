import urllib.request,sqlite3,json,string,re,BeautifulSoup

baseUrlPrefix = "http://www.thesaurus.com/browse/"
baseUrlSuffix = "?s=t"

def getSyn(word):
	synonList = []
	with urllib.request.urlopen( baseUrlPrefix+word+baseUrlSuffix):
		html = response.read()
		soup = BeautifulSoup(html)
		ulList = soup.findAll("ul"):
		result = soup.findAll('ul',{'class':"carouselActivate"})
		if result.indexOf("no thesaurus results") == -1:
			return -1
		for i in ulList:
			for li in i.findAll('li'):
				synonList.append(li)
	return synonList

def insertion(bibleSet):
	for i in bibleSet:
		s = list(bibleSet)[i]
		s = re.sub(r'[^\w\s]','',s)#strips off the punctuation
		synList = getSyn(s)
		if synList == -1:
			continue
def initDB():
    conn = sqlite3.connect("synon.db")
    c = conn.cursor()
    c.execute("DROP TABLE if exists mq")
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
