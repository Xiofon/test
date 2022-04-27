ic = [123,456,789,336,775,566]
i = [456,789,888,558,666,221]
mo = [9000,5000,6000,10000,12000,7000]
m = int(input("輸入查詢組數:"))
for a in range(0,m):
    s = str(input(""))
    x = int(s[0:4])
    y = int(s[4:8])
    ans = 0
    for b in range(0,6):
        if ic[b] == x:
            if i[b] == y:
                print(mo[b])
            else:
                print("error")
        else:
            ans += 1
        if ans == 6:
            print("error")