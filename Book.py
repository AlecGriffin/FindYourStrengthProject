__author__ = 'AlecGriffin'

class Book:

    def __init__(self, bookTitle):
        self.bookTitle = bookTitle

        # Container for Chapter Objects
        self.chapterList = []
        self.numChapters = 0

    def addChapter(self, chapter):
        self.numChapters += 1
        self.chapterList.append(chapter)

    def printBook(self):
            print(self.bookTitle)
            print()
            print()
            for chapter in self.chapterList:
                chapter.printChapter()