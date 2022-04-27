x = int(input("測試的資料量:"))
for a in range(0,x):
    bl = str(input(""))
    l = len(bl)
    c = 0
    b = 0
    while(True):
        c += 1
        if c >= l or bl[c] == " ":
            break
    da = bl[b:c]
    c += 1
    b = c
    while(True):
        c += 1
        if c >= l or bl[c] == " ":
            break
    ma = bl[b:c]
    c += 1
    b = c
    while(True):
        c += 1
        if c >= l or bl[c] == " ":
            break
    ch = bl[b:c]
    c += 1
    b = c
    if (da == "A" and ma == "B") or (da == "B" and ma=="A"):
        print("YES")
    elif (da == "O" and ma == "O" and ch=="O") or (ma == "O" and da == "O" and ch=="O"):
        print("YES")
    elif (da == "O" and ma=="A" and ch=="O") or (da == "A" and ma=="O" and ch=="O") or (da == "O" and ma=="A" and ch=="A") or (da == "A" and ma=="O" and ch=="A"):
        print("YES")
    elif (da == "O" and ma=="B" and ch=="O") or (da == "B" and ma=="O" and ch=="O") or (da == "O" and ma=="B" and ch=="B") or (da == "B" and ma=="O" and ch=="B"):
        print("YES")
    elif (da == "O" and ma=="AB" and ch=="A") or (da == "AB" and ma=="O" and ch=="A") or (da == "O" and ma=="AB" and ch=="B") or (da == "AB" and ma=="O" and ch=="B"):
        print("YES")
    elif(da == "A" and ma == "A" and ch=="A") or (da == "A" and ma == "A" and ch=="O"):
        print("YES")
    elif(da == "AB" and ma == "A" and ch=="A") or (da == "A" and ma == "AB" and ch=="A") or(da == "AB" and ma == "A" and ch=="B") or (da == "A" and ma == "AB" and ch=="B") or (da == "AB" and ma == "A" and ch=="AB") or (da == "A" and ma == "AB" and ch=="AB"):
        print("YES")
    elif(da == "B" and ma == "B" and ch=="B") or (da == "B" and ma == "B" and ch=="O"):
        print("YES")
    elif(da == "AB" and ma == "B" and ch=="B") or (da == "B" and ma == "AB" and ch=="B") or(da == "AB" and ma == "B" and ch=="B") or (da == "B" and ma == "AB" and ch=="B") or (da == "AB" and ma == "B" and ch=="AB") or (da == "B" and ma == "AB" and ch=="AB"):
        print("YES")
    elif (da == "AB" and ma == "AB" and ch =="B") or (da == "AB" and ma == "AB" and ch =="AB"):
        print("YES")
    else:
        print("IMPOSSIBLE")