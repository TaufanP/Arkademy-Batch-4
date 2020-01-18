"""
4.py, by Taufan Prihantoro, 2020-01-18
This program print pattern.
"""

# FUNGSI CETAK
def printPattern(n):
    if (type(n) == int):
        for i in range(0, n): 
            for j in range(0, n-1): 
                if (j==0):
                    print("* ",end="") 
                elif (i==(n/2)-0.5):
                    print("* ",end="")  
                else:
                    print("= ",end="")
            print("*  ")
    else:
        return 'Paramter harus angka dan ganjil!'
