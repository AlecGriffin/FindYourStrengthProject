__author__ = 'AlecGriffin'


class Chapter:
    def __init__(self, chapterNum):
        # Container for Verse Objects
        self.verseList = []
        self.numVerses = 0
        self.chapterNum = chapterNum

    def addVerse(self, verse):
        self.verseList.append(verse)
        self.numVerses += 1

    def getNumVerses(self):
        return self.numVerses

    def printChapter(self):
        for verse in self.verseList:
            print(self.chapterNum + "---", end="")
            verse.printVerse()
