import random
from random import randrange
b=[]
i=0
while i<10:
    a=random.randrange(0,10)
    if a not in b:
        b.append(a)
        i+=1
print(b)