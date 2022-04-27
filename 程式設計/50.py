all = ["John","Mary","Tina","Fiona","Claire","Eva","Ben","Bill","Bert"]
en = ["John","Mary","Fiona","Claire","Ben","Bill"]
ma = ["Mary","Fiona","Claire","Eva","Ben"]
ans = []
ans2 = []
ans3 = []
c = 0
for a in range(0,6):
    for i in range(0,5):
        if en[a] == ma[i]:
            ans.append(en[a])
print("英文及數學及格:{0}".format(ans))
for a in range(0,9):
    tf = True
    for i in range(0,5):
        if ma[i] == all[a]:
            tf = False
    if tf:
        ans2.append(all[a])
        c += 1
print("數學不及格:{0}".format(ans2))
for a in range(0,6):
    for i in range(0,c):
        if en[a] == ans2[i]:
            ans3.append(en[a])
print("英文及格且數學不及格:{0}".format(ans3))