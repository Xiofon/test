m = int(input())
d = int(input())
ans = (m*2+d)%3
if ans == 0:
    print("普通")
elif ans == 1:
    print("吉")
else:
    print("大吉")