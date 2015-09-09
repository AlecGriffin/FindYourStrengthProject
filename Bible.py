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

    # Returns a list of Strings in the format:  Book_Title --- Chapter_Number:Verse_Number --- "Verse"
    # def getRelevantVerses(self, inputKey):
    #     numTimesMentioned = 0
    #     # list of Lists     [Each List's Format]--> Book_Title --- Chapter_Num:Verse_Num --- "Verse"
    #     completeVerseList = []

    #     # Cycles through 66 books of the bible
    #     for bookTitle in self.bookDict.keys():

    #         # Cycles through the chapters of the bible
    #         for chapter in self.bookDict[bookTitle].chapterList:

    #             # Cyles through the verses on a specific chapter
    #             for verse in chapter.verseList:
    #                 verseWordList = verse.verseString.split()
    #                 individualVerse = []
    #                 individualVerse.append( bookTitle + " " + chapter.chapterNum + ":" + verse.verseNum)

    #                 # Cycles through the words of a specific verse
    #                 for word in verseWordList:
    #                     if(word.lower() == inputKey.lower()):
    #                         individualVerse.append(verse.verseString)
    #                         completeVerseList.append(individualVerse)
    #                         break

    #     return completeVerseList

    def getRelevantVerses(self, inputKey):

        # list of Lists     [Each List's Format]--> Book_Title --- Chapter_Num:Verse_Num --- "Verse"
        result = []
        completeVerseList = []
        analytics_numTimesMentioned = 0
        analytics_versesContainingWord = 0
        analytics_numVersesPerBookDict = {}
        analytics_numWordsPerBookDict =  {}

        # Cycles through 66 books of the bible
        for bookTitle in self.bookDict.keys():
            analytics_numVersesPerBookDict[bookTitle] = 0
            analytics_numWordsPerBookDict[bookTitle] = 0

            # Cycles through the chapters of the bible
            for chapter in self.bookDict[bookTitle].chapterList:

                # Cyles through the verses on a specific chapter
                for verse in chapter.verseList:
                    verseWordList = verse.verseString.split()
                    individualVerse = []
                    individualVerse.append( bookTitle + " " + chapter.chapterNum + ":" + verse.verseNum)

                    tempWordAppearances = 0
                    for word in verseWordList:
                        if(word.lower() == inputKey.lower()):
                            tempWordAppearances += 1
                            analytics_numTimesMentioned += 1
                            analytics_numWordsPerBookDict[bookTitle] += 1

                    if(tempWordAppearances > 0 ):
                        analytics_versesContainingWord += 1
                        analytics_numVersesPerBookDict[bookTitle] += 1
                        individualVerse.append(verse.verseString)
                        completeVerseList.append(individualVerse)

        result.append(analytics_numTimesMentioned) # Number of times inputkey is mentioned in the bible
        result.append(analytics_versesContainingWord) # Number of verses containing inputKey
        result.append(analytics_numWordsPerBookDict) # Number of times inputkey appears in each book (Stored in a dictionary)
        result.append(analytics_numVersesPerBookDict) # Number of verses containing inputKey per Book (Stored in a dictionary)
       
        result.append(completeVerseList) # List of verseLists
        return result # ^^^List containing all of the above^^^



    def printBible(self):
        for bookName in self.bookDict.keys():
            self.bookDict.get(bookName).printBook()

    def printBook(self, bookTitle):
        self.bookDict[bookTitle].printBook()


