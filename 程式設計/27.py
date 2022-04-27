import string
while(True):
    x = str(input("輸入整數數列(end結束):"))
    ans = "0"
    if x == "end" :
        break
    for a in range(0,len(x)):
        for b in range(len(x)-1,a,-1):
            y = x[a:b+1]
            if a == 0:
                z = x[b::-1]
            else:
                z = x[b:a-1:-1]
            if y == z  and len(y) > len(ans):
                ans = y
            if int(ans) > int(y) and len(y) == len(ans) and y == z:
                ans = y
    print(ans)
