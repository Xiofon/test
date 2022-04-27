import string
a = str(input("請輸入正整數:"))
l = len(a)
ans = 0
for b in range(l):
    for c in range(l-b):
        d = int(a[b:l-c])
        e = 0
        for i in range(2,d):
            if d % i == 0 :
                e += 1
                break
        if (e==0) and (ans<d) and(d!=1):
            ans = d
if ans == 0:
    print("No prime found")
else:
    print(ans)          
        