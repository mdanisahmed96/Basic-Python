"""
#stack
books=[]
books.append("learn c ")
books.append("learn c++ ")
books.append("learn python ")
books.append("learn java ")
print(books)
books.pop()
print(books)
"""
#queue
from collections import deque

bank = deque (["anis","anis1","anis2"])

print(bank)
bank.popleft()
print(bank)