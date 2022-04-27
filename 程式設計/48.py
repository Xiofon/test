n = int(input("輸入比數n:"))
# n = 4
ce = {}
for i in range(0,n):
    z = str(input())
    # z = "Dog 狗"
    a = 0
    while(True):
        a += 1
        if z[a] == " ":
            break
    en = z[0:a]
    ch = z[int(a+1):len(z)]
    ce[en] = ch
ans = str(input("輸入欲查詢單字"))
print("{0}中文意思為{1}" .format(ans,ce[ans]))