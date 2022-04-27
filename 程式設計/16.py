import string
while(True):
    x = str(input(""))
    x1 = str(input("")) 
    x2 = int(input(""))
    s = []
    s1 = []
    b = 0
    c = 0
    for a in range(0,5):
        while(True):
            if b==len(x) or x[b] == " " :
                break
            b += 1 
        s.append(x[c:b])
        c = b+1
        b +=1
    b = 0
    c = 0
    for a in range(0,5):
        while(True):
            if b==len(x1) or x1[b] == " " :
                break
            b += 1 
        s1.append(x1[c:b])
        c = b+1
        b +=1
    num = []
    num1 = []
    for a in range(0,13):
        num.append(0)
        num[a] =0
        num1.append(0)
        num1[a] =0
    fl = []
    fl1 = []
    for a in range(0,4):
        fl.append(0)
        fl[a] =0
        fl1.append(0)
        fl1[a] =0
    ans = []
    ans1 = []
    for a in range(0,7):
        ans.append(0)
        ans[a] = 0
        ans1.append(0)
        ans1[a] = 0
    for a in range(0,5):
        t = s[a]
        if t[0] =="S":
            fl[0] += 1
        elif t[0] =="H":
            fl[1] += 1
        elif t[0] == "D":
            fl[2] += 1
        else:
            fl[3] += 1
        t = s1[a]
        if t[0] =="S":
            fl1[0] += 1
        elif t[0] =="H":
            fl1[1] += 1
        elif t[0] == "D":
            fl1[2] += 1
        else:
            fl1[3] += 1
    for a in range(0,5):
        t = s[a]
        if len(t) == 3:
            t = int(t[1:3])
        else:
            t = int(t[1])
        num[t-1] += 1
        t = s1[a]
        if len(t) == 3:
            t = int(t[1:3])
        else:
            t = int(t[1])
        num1[t-1] += 1
    for a in range(0,4):
        if fl[a] == 5:
            if num[0] and num[12] and num[11] and num[10] and num[9]:
                ans[0] = 1
            else:
                for b in range(0,9):
                    if num[b]  and num[b+1]  and num[b+2] and num[b+3] and num[b+4]:
                        ans[0] = 1

        if fl1[a] == 5:
            if num1[0] and num1[12] and num1[11] and num1[10] and num1[9]:
                ans[0] = 1
            else:
                for b in range(0,9):
                    if num1[b]  and num1[b+1]  and num1[b+2] and num1[b+3] and num1[b+4]:
                        ans[0] = 1
    for a in range(0,13):
        if num[a] == 4:
            ans[1] = 1
        if num1[a] == 4:
            ans1[1] = 1

    
    for a in range(0,13):
        if num[a] == 3:
            tf = True
            for b in range(0,13):
                if num[b] == 2:
                    tg = False
                    ans[2] = 1 
            if tf :
                ans[4] = 1
        if num1[a] == 3:
            tf = True
            for b in range(0,13):
                if num1[b] == 2:
                    tg = False
                    ans1[2] = 1 
            if tf :
                ans1[4] = 1
     
    if num[0] and num[12] and num[11] and num[10] and num[9]:
        ans[3] = 1
    else:
        for b in range(0,9):
            if num[b] and num[b+1]  and num[b+2] and num[b+3] and num[b+4]:
                ans[3] = 1
    if num1[0] and num1[12] and num1[11] and num1[10] and num1[9]:
            ans1[3] = 1
    else:
        for b in range(0,9):
            if num1[b] and num1[b+1]  and num1[b+2] and num1[b+3] and num1[b+4]:
                ans1[3] = 1
    for a in range(0,13):
        if num[a] == 2:
            ans[6] +=1
            if ans[6] ==2:
                ans[5] = 1
                ans[6] = 0
        if num1[a] == 2:
            ans1[6] += 1
            if ans1[6] ==2:
                ans1[5] = 1
                ans1[6] = 0
    win = 7
    win1 = 7
    for a in range(0,7):
        if ans[a] == 1:
            win = a
        if ans1[a] == 1:
            win1 = a
    if win > win1:
        print("0")
    else:
        print("1")
    if x2 == -1:
        break