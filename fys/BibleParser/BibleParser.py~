__author__ = 'AlecGriffin'

from Verse import Verse
from Bible import Bible
from Chapter import Chapter
from Book import Book

def runParse():
	bookName = ""

	bible = Bible()
	book = Book("Genesis")
	chapter = Chapter(1)

	file = open("bible.txt")
	bookname = ""
	for line in  file:
	    splitLine = line.split()

	    # Aquires Book Title Name of current line
	    if (splitLine[0].isdigit()):
		  bookName = splitLine[0] + " " + splitLine[1]
	    elif (splitLine[0] == "Song"):
		  bookName = splitLine[0] + " " + splitLine[1] + " " + splitLine[2]
	    else:
		  bookName = splitLine[0]

	    # Aquires Book Chapter number and verse number of current line
	    if (splitLine[0].isdigit()):
		  chapNumAndVerseNum = splitLine[2].split(sep=":")
	    elif (splitLine[0] == "Song"):
		  chapNumAndVerseNum = splitLine[3].split(sep=":")
	    else:
		  chapNumAndVerseNum = splitLine[1].split(sep=":")

	    # Uses chapNumandVerseNum to get the chapter number
	    # and the verse Number
	    currentChapNum = chapNumAndVerseNum[0]
	    currentVerseNum = chapNumAndVerseNum[1]

	    verseString = ""

	    # Aquires the Verse String from the current line.
	    if (splitLine[0].isdigit()):
		  for index in range(3, len(splitLine)):
		      verseString += splitLine[index] + " "
	    elif (splitLine[0] == "Song"):
		  for index in range(4, len(splitLine)):
		      verseString += splitLine[index] + " "
	    else:
		  for index in range(2, len(splitLine)):
		      verseString += splitLine[index] + " "

	    # Uses generated verse String to create a new bible verse
	    currentBibleVerse = Verse(currentVerseNum, verseString)

	    # When Book Title Changes, add the current book to the bible.
	    # Then, create new book.
	    if (book.bookTitle != bookName):
		  book.addChapter(chapter)
		  chapter = Chapter(currentChapNum)
		  bible.addBook(book.bookTitle, book)
		  book = Book(bookName)  # Resets Book Object
		  book.bookTitle = bookName

	    # When Book Number Changes, add the current chapter to the current book
	    # Then, Create a new book.
	    elif(currentChapNum != chapter.chapterNum):
		book.addChapter(chapter)
		chapter = Chapter(currentChapNum)

	    # Adds each verse to the correct chapter
	    chapter.addVerse(currentBibleVerse)

	# Adds Revelations [Edge Case]
	book.addChapter(chapter)
	bible.addBook(bookName, book)
	return bible
