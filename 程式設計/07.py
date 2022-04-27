import string
import math
x = str(input("輸入月租費型式與通話時間:"))
l = len(x)
y = int(x[4:l])
x = int(x[0:3])
ans = 0
if x == 186:
    ans = y * 0.09
    ans = round(ans,0)
    if  ans > x and ans <= 2*x:
        ans *= 0.9
    if ans > 2*x :
        ans *= 0.8
elif x == 386:
    ans = y * 0.08
    ans = round(ans,0)
    if  ans > x and ans <= 2*x:
        ans *= 0.8
    if ans > 2*x :
        ans *= 0.7
elif x == 586:
    ans = y * 0.07
    ans = round(ans,0)
    if  ans > x and ans <= 2*x:
        ans *= 0.7
    if ans > 2*x :
        ans *= 0.6
elif x == 986:
    ans = y * 0.06
    ans = round(ans,0)
    if  ans > x and ans <= 2*x:
        ans *= 0.6
    if ans > 2*x :
        ans *= 0.5
ans = round(ans,0)
ans1 = str(ans)
a = 0
while(True):
    a +=1
    if ans1[a] == ".":
        ans1 = ans1[0:a]
        break
print("通話費為:{0}" .format(ans1))