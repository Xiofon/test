import string
x = str(input("輸入一整個續串列為:"))
num = []
c = 0
b = 0
a = 0
while(b <= len(x)):
    while (b <= len(x)):
        b += 1
        if b >= len(x) or x[b] == " ":
            break
    if b <= len(x):
        num.append(int(x[a:b]))
        c += 1
    a = b
ans=[]
for a in range(0,c):
    ans.append(0)
for a in range(0,c):
    for b in range(0,c):
        if num[a]==num[b]:
            ans[a] +=1
ans2 = True
for a in range(0,c):
    if ans[a] > c / 2:
        print("過半元素為:{0}".format(num[a]))
        ans2 = False
        break
if ans2 :
    print("No") 