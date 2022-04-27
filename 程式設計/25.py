n = str(input("請輸入考試次數及學生數:"))
m = str(input("每次考試所佔的比例:"))
student = int(n[2])
test = int(n[0])
test1 = []
b = 0
a = 0
ans = 0
for i in range(0,test):
    b += 4
    test1.append(float(m[a:b]))
    a = b
for i in range(0,student):
    x = str(input())
    student1 = []
    a = 0 
    b = 0
    for z in range(0,test):
        while(True):
            b += 1
            if b == len(x) or x[b] == " ":
                break
        student1.append(int(x[a:b]))
        a = b
    for z in range(0,test):
        ans += (student1[z]*test1[z])
ans /= student
ans = round(ans,2)
print("全班總平均為:{0}" .format(ans))