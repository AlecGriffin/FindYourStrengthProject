import pickle
import os.path
import Bible

def search(bible, userInput):
    versesAndAnalyticInfo = []
    if (os.path.isfile('bible_data.pkl')):
        with open('bible_data.pkl','wb') as output:
            pickle.dump(bible,output,pickle.HIGHEST_PROTOCOL)

    versesAndAnalyticInfo = bible.getRelevantVerses(userInput)
    return versesAndAnalyticInfo
