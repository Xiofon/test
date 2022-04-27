km = float(input("請輸入路程公里數(km):"))
a = 0.25
ans = 75
if km < 1.5:
    print("所需車資為:75")
else:
    km -= 1.5
    while(True):
        if a > km:
            break
        a += 0.25
        ans += 5
    if a != km:
        ans += 5
    print("所需車資為:{0}".format(ans))
