x = int(input("搭了幾次電梯:"))
n = 1
ans = 0
for i in range(0,x):
    a = int(input(""))
    if n > a:
        ans += (n-a) * 10
    else:
        ans += (a - n) * 20
    n = a
print("{0}元".format(ans))