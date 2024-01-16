i=1
j=9
for i in range(9):
    print(i*"#",end="")
    for j in range(9):
        print(j*" ",i*"#")
        j-=1
    i+=1