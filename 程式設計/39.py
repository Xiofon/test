x = int(input())
b = 0
for i in range(0,x):
    m = int(x / 2)+1
    b += 1
    n = m - b
    if n > 0:
        for a in range(0,n):
            print(" ",end="")
        for z in range(1,x-a*2-1):
            print("*",end="")
        print()
    elif n == 0 :
        for a in range(0,x):
            print("*",end="")
        print()
    else:
        for a in range(0,n,-1):
            print(" ",end="")
        for z in range(1,x+a*2-1):
            print("*",end="")
        print()
    
    
    