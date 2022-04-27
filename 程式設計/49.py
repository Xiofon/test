st = str(input("請輸入英文句子:"))
st = "an apple a day keeps the doctor away"
s = []
a = 0
b = 0
c = 0
while(True):
    while(True):
        b += 1
        if b>=len(st) or st[b] == " ":
            break
    a += 1
    s.append(st[c:b])
    c = b + 1
    if b >= len(st):
        break
print("輸出結果:[",end="")
for i in range(a-1,0,-1):
    print("'{0}'".format(s[i]),end=",")
print("'{0}']" .format(s[0]))
