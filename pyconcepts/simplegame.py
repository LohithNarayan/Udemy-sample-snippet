
from random import shuffle

def shuffle_list(mylist):
    shuffle(mylist)
    return mylist

def player_guess():
    
    guess=''
    while guess not in ['0','1','2']:
        guess=input('pick a number:0,1 or 2')
    return int(guess)   

def check_guess(mylist,guess):
    if mylist[guess]=='O':
        print('correct guess ')
    else:
        print('wrong guess')
        print(mylist)

#MAIN LOGIC TO CALL IN PY FILE
#INITIAL LIST
mylist=['','O','']
#SHUFFLE LIST
mixedup_list=shuffle_list(mylist)
#USER GUESS
guess=player_guess()
#CHECK GUESS  
check_guess(mixedup_list,guess)
