import urllib.request,urllib.error,sqlite3,json,string,re
from bs4 import BeautifulSoup

baseUrlPrefix = "http://www.thesaurus.com/browse/"
baseUrlSuffix = "?s=t"

def getSyn(word):
	synonList = []
	try:
		with urllib.request.urlopen( baseUrlPrefix+word+baseUrlSuffix) as response:
			html = response.read()
			soup = BeautifulSoup(html)
			ulList = soup.findAll("ul")
			#print(ulList)
			result = soup.findAll('ul',{'class':"carouselActivate"})
			if "no thesaurus results"  in str(result):
				print("here")
				return -1
			for i in ulList:
				#print(i)
				for li in i.findAll('a'):
					#Too lazy to use Regex
					if "%" not in str(li) and "?" not in str(li) and "}" not in str(li) and ";" not in str(li) and "#" not in str(li) and "dictionary.com" not in str(li) and "dictionary.reference" not in str(li):
						synonList.append(li.getText().replace('\n',''))
						#print(li.getText().replace('\n',''))
	except urllib.error.HTTPError:
		return -1
		#print(synonList)
	return synonList

def insertion(bibleSet):
	counter = 0
	for i in bibleSet:
		counter  = counter +1
		#print(counter)
		s = i
		s = re.sub(r'[^\w\s]','',s)#strips off the punctuation
		synList = getSyn(s)
		if synList == -1:
			text ="-1"
		else:
			text = (" ".join(synList))
		conn = sqlite3.connect("synon.db")
		c = conn.cursor()
		try:
			c.execute("INSERT INTO Synon(word,list) VALUES(?,?)",(s,text))
		except sqlite3.IntegrityError:
			conn.close()
			continue
		conn.commit()
		conn.close()

def initDB():
    conn = sqlite3.connect("synon.db")
    c = conn.cursor()
    c.execute("DROP TABLE if exists Synon")
    c.execute('CREATE TABLE Synon(word TEXT Primary Key, list TEXT)')
    conn.commit()
    conn.close()

if __name__=="__main__":
	f = open("bible.txt")
	bibleList = list(set(f))
	#print bibleList[1]
	bibleSet = set()
	for i in bibleList:
		i = i.lower()
		mylist = (i.split("	")[1]).split()
		bibleSet |= set(mylist)
	initDB()
	print(len(bibleSet))
	insertion(bibleSet)
	#getSyn("happy")
