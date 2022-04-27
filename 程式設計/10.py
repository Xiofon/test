import string
a = str(input("輸入N及M:"))
num = []
b = 0
while(True):
    b += 1
    if a[b] == " ":
        break
n = int(a [0:b])
m = int(a [b+1:len(a)])
for i in range(n):
    num.append([])
for i in range(n):
    x = str(input("輸入矩陣數值第{0}列:".format(i+1)))
    b = 0
    c = 0
    e = 0
    while (e<m):
        l = len(x)
        while (True):
            b += 1
            if b >=l or x[b] == " " :
                break
        num[i].append(int(x[c:b]))
        c = b
        b += 1
        e += 1
for b in range(0,m):
    print("輸出矩陣第{0}列數值為:".format(1+b),end=" " )
    for c in range(0,n):
        print(num[c][b],end=" " )
    print()