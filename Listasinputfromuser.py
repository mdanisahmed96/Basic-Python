"""
n= input("enter the number : ")
list =n.split()
sum=0 

for num in list:
    sum=sum + int (num)
print(sum)
"""
numofword=0
numofletter=0
numofdigit=0

text=input("enter a text of number : ")

for x in text:
    x=x.lower()
    if x>='a' and x<='z':
        numofletter=numofletter+1
    elif x>='0' and x<='9':
        numofdigit=numofdigit+1
    elif x==' ':
        numofword=numofword+1

print(numofletter)
print(numofdigit)
print(numofword)