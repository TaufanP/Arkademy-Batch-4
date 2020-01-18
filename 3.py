"""
3.py, by Taufan Prihantoro, 2020-01-18
This program count words in a sentence and assure the input is a string.
"""

# IMPORT REGEX
import re

# FUNGSI HITUNG DAN CEK
def wordCounter(word):

    if (type(word) == str):
        wordTemp = []
        allWord = re.split('\s',word)
        splitWord = re.split('\s',word)
        wordTemp = splitWord
        for i in range(0,len(wordTemp)-1):
            number = re.findall('\d',wordTemp[i])
            if(len(number)==0):
                continue
            else:
                (splitWord.remove(splitWord[i]))
        splitLen = len(splitWord)
        print(splitLen,end="/")
        print(len(allWord))

    else:
        return 'Parameter harus string!'
