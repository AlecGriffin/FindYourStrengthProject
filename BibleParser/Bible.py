__author__ = 'AlecGriffin'


class Bible:
    def __init__(self):
        self.bookDict = {}
        self.numBooks = 0

    # Adds a book the bible class if the book is not currently present in the bookDict
    def hasBook(self, bookTitle):
        return True if bookTitle in self.bookDict else False

    def getBook(self, bookTitle):
        return self.bookDict[bookTitle]

    # Return 1 if add was successful
    # Returns -1 if add was not successful
    def addBook(self, bookTitle, book):
        if (self.hasBook(bookTitle) == False):
            self.bookDict[bookTitle] = book
            self.numBooks += 1
            return 1
        else:
            return -1

    def printBible(self):
        for bookName in self.bookDict.keys():
            self.bookDict.get(bookName).printBook()

    def printBook(self, bookTitle):
        self.bookDict[bookTitle].printBook()
