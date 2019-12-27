for i in range(1,10):
    for k in range(1,i):
        print(end="       ")
    for j in range(i,10):
        print("%d*%d=%2d" % (i,j,i*j),end=" ")
    print("")
#第二种
for i in range(1,10):
    for k in range(1,i):
        print(end="        ")
    for j in range(i,10):
        print("{0:1}×{1:1}={2:<2}".format(i,j,i*j),end=' ')
    print("")
