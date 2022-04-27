import string
x = str(input("輸入值為:"))
l = len(x)
num = []
c = 0
for a in range(0,l):
    if x[a] != "," :
        num.append(int(x[a]))
        c+=1
num.sort()
max = 0
min = 0
for a in range(0,c):
    max = max + 10**a*num[a]
for a in range(c-1,-1,-1):
    min = min + 10**a*num[c-1-a]
ans = max - min
print("最大值數列與最小值數列差值為:{0}".format(ans))