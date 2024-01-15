try:
    a=int(input("enter a num : "))
    i=2
    while True:
        if a<2:
            print("rong int")
            a=int(input("enter a num: "))
        else:
            break
    while i<a:
        if a/i==int(a/i):
            print("not_prime")
            break
        i+=1
    else:
        print("prime")
except ValueError:
    print("rong something")
    a=input("enter a num: ")
    while True:
        if a!=int(a):
            print("rong something")
            a=input("enter a num: ")
        else:
            break
    i=2
    while True:
        if a<2:
            print("rong int")
            a=int(input("enter a num: "))
        else:
            break
    while i<a:
        if a/i==int(a/i):
            print("not_prime")
            break
        i+=1
    else:
        print("prime")
    

        


