import pickle
import os.path

def search(bible):
    verses = []
    if (os.path.isfile('bible_data.pkl')):
        with open('bible_data.pkl','wb') as output:
            pickle.dump(bible,output,pickle.HIGHEST_PROTOCOL)
    return verses
