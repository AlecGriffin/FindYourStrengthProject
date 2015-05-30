import pickle
import os.path
import Bible

def search(bible, userInput):
    verses = []
    if (os.path.isfile('bible_data.pkl')):
        with open('bible_data.pkl','wb') as output:
            pickle.dump(bible,output,pickle.HIGHEST_PROTOCOL)

    # How do I get word here??? 
    verses = bible.getRelevantVerses(userInput)
    return verses
