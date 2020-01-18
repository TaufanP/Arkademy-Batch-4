"""
5.py, by Taufan Prihantoro, 2020-01-18
This program create a series of numbers.
"""

# FUNGSI DERET
def sequenceT(x,y):
    if (x>y):
        last = [y]
        i=0
        while(last[-1]>1):
            last.append((last[i]**2) % (x+i))
            i+=1
        print('array: ' + str(last))
        print('count: ' + str(len(last)))
    else:
        return 'Parameter x harus lebih besar dibanding parameter y!'
