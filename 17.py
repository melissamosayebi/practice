def tavan(x,y):
    if y==0:
        return 1 
    else:
        return x*tavan(x,y-1)
print(tavan(2,4))