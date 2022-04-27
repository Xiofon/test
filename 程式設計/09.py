import string
x = str(input("輸入s1:"))
y = str(input("輸入s2:"))
l1 = len(x)
l2 = len(y)
ans = False
for a in range(0,l2-l1):
    if x == y[a:l1+a]:
        ans = True
        break
if ans:
    print("Yes")
else:
    print("No")