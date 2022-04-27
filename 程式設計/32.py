mo = int(input("小明身上有幾元:"))
x = int(input("販賣機有機種飲料:"))
ans = 0
for a in range(0,x):
    pr=int(input(""))
    if mo >= pr:
        ans += 1
print(ans)