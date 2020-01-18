"""
2.py, by Taufan Prihantoro, 2020-01-18
This program validating username and password from user.
"""

# IMPORT REGEX
import re

# FUNGSI VALIDASI USERNAME
def usernameValidity(username):
    # Panjang username
    userLen = len(username)

    # Seleksi username sesuai syarat
    if(userLen >= 5 and userLen <= 12):
        firstLetter = username[0]
        checkFL = re.findall('\A[a-z]', username)
        underScore = re.findall('[\W]', username)
        fLetterLen=len(checkFL)
        underScoreLen=len(underScore)
        if(fLetterLen > 0 and underScoreLen == 0):
            return True
        else:
            return False
    else:
        return ('Username 5 hingga 12 karakter!')
    
# FUNGSI VALIDASI USERNAME
def passwordValidity(password):
    
    # Panjang password
    passLen = len(password)
    
    # Seleksi username sesuai syarat
    if(passLen == 7):
        capital = re.findall('[A-Z]', password)
        regular = re.findall('[a-z]', password)
        number = re.findall('[0-9]', password)
        symbol = re.findall('[\w]', password)

        capitalLen = len(capital)
        regularLen = len(regular)
        numberLen = len(number)
        symbolLen = len(symbol)

        if(capitalLen == 5 and regularLen == 0 and numberLen == 1 and symbolLen ==6):
            return True
        else:
            return False
    else:
        return ('Password 7 karakter!')
