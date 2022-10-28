from re import I
from matplotlib import pyplot as plt



word1 = 2
word2 = 4
word3 = 6
word4 = -2
word5 = 10
I = 0
x = 0
## Oppgave 1##

'''
Opprett en while loop som kan:

1.-Opprett en lista med de variablene ovenfor
2.-Summere verdien til alle variablene
3.-Printe verdien i terminalen.

'''

min_liste = [word1, word2, word3, word4, word5]
print(min_liste)

while I < len(min_liste): 
    print(min_liste[I])
    I +=1
    