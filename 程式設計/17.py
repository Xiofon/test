x = str(input(""))
b = 0
while(True):
    b+=1
    if x[b] == " ":
        break
n = int(x[0:b])
m = int(x[b:len(x)])
nu = []
for a in range(0,n):
    nu.append([])
for a in range(0,n):
    s = str(input(""))
    c = 0
    d = 0
    for b in range(0,m):
        while(len(s)>c):
            c += 1
            if c >=len(s) or s[c] == " ":
                break
        nu[a].append(int(s[d:c]))
        d = c

y = str(input(""))
b = 0
while(True):
    b+=1
    if y[b] == " ":
        break
n1 = int(y[0:b])
m1= int(y[b:len(y)])
nu1 = []
for a in range(0,n1):
    nu1.append([])
for a in range(0,n1):
    s = str(input())
    c = 0
    d = 0
    for b in range(0,m1):
        while(len(s)>c):
            c += 1
            if c >=len(s) or s[c] == " ":
                break
        nu1[a].append(int(s[d:c]))
        d = c
if n1 == n and m1 == m:
    for b in range(0,n):
        for a in range(0,m):
            ans = nu[b][a]+nu1[b][a]
            print(ans,end=" ")
        print()
else:
    print("兩個矩陣無法相加")