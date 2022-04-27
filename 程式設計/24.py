x = int(input("請輸入陣列大小:"))
n = [[60,50,30],[100,10,90],[80,40,20]]
ans = 0
ans1 = []
for i in range(0,x):
    ans1.append(0)
for i in range (0,3):
    for a in range(0,3):
        for b in range(0,x):
            if ans1[b] < n[i][a]:
                if b != 2:
                    ans1[b+1] = ans1[b]
                ans1[b] =  n[i][a]
                break

for i in range(0,3):
    ans += ans1[i]
print("最大值為:{0}" .format(ans))
print("位置為",end="")
for i in range (0,3):
    for a in range(0,3):
        for b in range(0,x):
            if ans1[b] == n[i][a]:
                print("({0},{1})" .format(i+1,a+1) ,end="")
                break
            
print()
