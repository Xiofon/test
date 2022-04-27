import string
x = int(input("輸入第一行正整數:"))
y = str(input("第二行數列中的數:"))
c = 0
a = 0
b = 0
num=[]
ans = []
while(c<x):
    e = y[b]
    while(b != len(y)):
        e = y[b]
        if e == " ":
            break 
        b += 1
    num.append(int(y[a:b]))
    c += 1
    a = b
    b += 1
for a in range(0,x):
    ans.append(0)
for a in range(0,x):
    ans[num[a]-1] += 1
ans1 = 0
ans2 = 0
ans3 = 0
for a in range(0,x):
    if ans[a] == 1:
        ans3 += 1
    if ans2 < ans[a]:
        ans1 = a
        ans2 = ans[a]
if ans3 == x:
    print("每個數字剛好只出現過一次")
else:
    print("最大出現數字{0}:".format(ans1+1))
    print("出現次數為:{0}".format(ans2))