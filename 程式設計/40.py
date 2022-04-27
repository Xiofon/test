nu = int(input(""))
x = int((nu - 1) / 4)
for a in range(0,nu-2,2):
    for i in range(0,x):
        print(" ",end="")
    print(a+1)
for a in range(0,nu,2):
    print(a+1,end="")
print()
for a in range(nu-3,-1,-2):
    for i in range(0,x):
        print(" ",end="")
    print(a+1)