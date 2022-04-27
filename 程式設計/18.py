import string
x = str(input())
l = len(x)
num = []
c = 0
b = 0
for a in range(0,5):
    
    while(True):
        c += 1
        if c >= l or x[c] == " ":
            break
    num.append(x[b:c])
    c += 1
    b = c
ans = 0
for a in range(0,5):
    if num[a] == "A":
        ans +=1
    elif num[a] == "J":
        ans += 11
    elif num[a] == "Q":
        ans += 12
    elif num[a] == "K":
        ans += 13
    else:
        ans += int(num[a])
print(ans)