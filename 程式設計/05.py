m = int(input("請輸入階層值M:"))
ans = 1 
for a in range(1,m):
    ans *= a
    if ans > m:
        break
print("超過M為{0}的最小N階層值為:{1}".format(m,a))
