sc = ["國文","英文","微積分","體育","程式設計"]
f = []
ans = 0
for a in range(0,5):
    print(sc[a],end="")
    f.append(int(input(":")))
    ans += f[a]
ans /= 5
ans = round(ans,2)
ans1 = str(ans)
c = 0
while(True):
    c += 1
    if ans1[c] == ".":
        break
c += 1
if len(sc) - 1 - c == 2:
    print("平均分數{0}" .format(ans))
elif len(sc) - 1 - c == 1:
    print("平均分數{0}0" .format(ans))
elif len(sc) - 1 - c == 0:
    print("平均分數{0}.00" .format(ans))

big = 0
small = 100
for a in range(0,5):
    if f[a] > big:
        big = f[a]
    if f[a] < small:
        small = f[a]
for a in range(0,5):
    if big == f[a]:
        print("最高分科目:{0}{1}分" .format(sc[a],f[a]))
for a in range(0,5):
    if small == f[a]:
        print("最低分科目:{0}{1}分" .format(sc[a],f[a]))
        break