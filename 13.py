def integer_number(x):
    if x<=0:
        print(0,end=" ")
    else:
        print(-x,end=" ")
        integer_number(x-1)
        print(x,end=" ")
integer_number(4)