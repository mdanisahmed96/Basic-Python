from random import randint
for x in range (1,6):   
    guessnum = int(input("enter your guess number 1 to 5 : "))
    randomnum=randint(1,5)
    if guessnum==randomnum:
        print("yes")
    else:
        print("NO")
        print("random the number : ",randomnum)