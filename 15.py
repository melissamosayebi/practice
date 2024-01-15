x=int(input("enter a num between 1,10 : "))
while True:
    if 0<x<11:
        print("well done")
        break
    else:
        try:
            print("try again")
            x=int(input("enter a num between 1,10 : "))
        except ValueError:
            print("pleas enter a intiger number")

