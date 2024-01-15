try:
    n=int(input("how many? "))
    a=[]
    i=0
    while i<n:
        b=input("enter a num: ")
        a.append(b)
        i+=1
    print(a[ : :-1])
except ValueError:
    print("rong num")
    n=input("how many? ")
    if n!=int(n):
        while n!=int(n):
            n=int(input("how many? "))
    a=[]
    i=0
    while i<n:
        b=input("enter a num: ")
        a.append(b)
        i+=1
    print(a[ : :-1])