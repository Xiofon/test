m = int(input("組數為:"))
for a in range(0,m):
    x = str(input("第{0}組:".format(a+1)))
    b = 0
    while(True):
        b+=1
        if x[b] == " ":
            break
    x1 = int(x[0:b])
    x2 = int(x[b:len(x)])
    ans = x1 * 250 + x2 * 175
    print("第{0}應收費用:{1}".format(a+1,ans))