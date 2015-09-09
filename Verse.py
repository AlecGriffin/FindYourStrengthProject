__author__ = 'AlecGriffin'


class Verse:
    def __init__(self, verseNum, verseString):
        self.verseNum = verseNum
        self.verseString = verseString

    def printVerse(self):
       print(self.verseNum + ": " + self.verseString)

