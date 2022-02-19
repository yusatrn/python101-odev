
from tkinter import Y


yedeklist = []
    
def flat(l):
    for i in l:
        if type(i)==list:
            flat(i)
        else:
            yedeklist.append(i)

flat([[1,'a',['cat'],2],[[[3]],'dog'],4,5])
print(yedeklist)

# reverse 

x = [[1, 2], [3, 4], [5, 6, 7]]
yedek = []

def ters(l):
    for i in l:
        if type(i)==list:
            yedek.append(list(reversed(i)))
            
            
        

ters([[1, 2], [3, 4], [5, 6, 7]])
print(list(reversed(yedek)))
