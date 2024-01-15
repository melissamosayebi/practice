x=int(input(": "))
def find_lst(a):
    if x in a:
        print(a.index(x))
    else:
        print("your num isn't in list")
find_lst([4,5,8,3,6,1,9,7])