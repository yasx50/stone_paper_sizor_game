#  stone paper sizor game
# author YASH YADAV


import random

def win(comp,you):
    if you==comp:
        return None
    if comp=='s':
        you='p'
        return True
    elif you=='S':
        return False
    if comp=='p':
        you='S'
        return True
    elif you=='s':
        return False
    if comp=='S':
        you='s'
        return True
    elif you=='p':
        return False
    
print("computer turn is completed now yours\n choose")
randomno=random.randint(1,3)
if randomno==1:
    comp='s'
elif randomno==2:
    comp='p'
elif randomno==3:
    comp='S'


you=input("for stone(s),for paper(p),for sizors(S)\n")
a=win(comp,you)


print(f"computer choose  {comp} and you choose  {you}")


if a==None:
    print("this game is tie :| ")
if a==False:
    print("you win this game :)")
if a==True:
    print("you loose the game :< ")



