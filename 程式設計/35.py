sA = str(input("sA:"))
sB = str(input("sB:"))
l = len(sA)
tf = True
for a in range(0,len(sB)-l):
    if sB[a:a+l] == sA:
        print("子字串判斷為:Yes")
        tf = False
        break
if tf:
    print("子字串判斷為:No")
    