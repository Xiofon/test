n = str(input("輸入矩陣維度:"))
a = 0
while(True):
    a += 1
    if n[a] == " ":
        break
x = int(n[0:a])
y = int(n[a+1:len(n)])
a1 = []
for a in range(0,x):
    a1.append([])  
for a in range(0,x):
    n = str(input(""))
    c = 0
    d = 0
    for b in range(0,y):
        while(True):
            c += 1
            if c >= len(n) or n[c] == " ":
                break
        g = int(n[d:c])
        a1[a].append(g)
        d = c
a2 = []
for a in range(0,x):
    a2.append([])  
for a in range(0,x):
    n = str(input(""))
    c = 0
    d = 0
    for b in range(0,y):
        while(True):
            c += 1
            if c >= len(n) or n[c] == " ":
                break
        g = int(n[d:c])
        a2[a].append(g)
        d = c

for a in range(0,x):
    for b in range(0,y):
        print(a1[a][b]*a2[a][b],end=" ")
    print()