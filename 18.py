i=1
j=34
for i in range(9):
    print(i*"🟫",end="")
    print(j*" ",end="")
    j-=4
    print(i*"🟫")
#j=i*4+2