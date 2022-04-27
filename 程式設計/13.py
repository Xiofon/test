import string
s = str(input("輸入一個字元:"))
ans = s[len(s)::-1]
if s == ans :
    print("Yes")
else:
    print("No")