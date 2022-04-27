import string
ans = str(input(""))
while(True):
    x = str(input(""))
    if x == "0000":
        break
    a = 0 
    b = 0
    for i in range(0,4):
        for z in range(0,4):
            if x[z] == ans[i] and z == i:
                a += 1
                break
            elif x[z] == ans[i]:
                b += 1
                break
    print("{0}A{1}B" .format(a,b))