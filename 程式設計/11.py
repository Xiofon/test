import string
x = str((input("輸入月及日:")))
m = int(x[0:2])
d = int(x[3:5])
print("星座為:",end="")
if m == 1:
    if d <= 20:
        print("Capricorn")
    else:
        print("Aquarius")
elif m == 2:
    if d <= 18:
        print("Aquarius")
    else:
        print("Pisces")
elif m == 3:
    if d <= 21:
        print("Pisces")
    else:
        print("Aries")
elif m == 4:
    if d <= 20:
        print("Aries")
    else:
        print("Taurus")
elif m == 5:
    if d <= 21:
        print("Taurus")
    else:
        print("Gemini")
elif m == 6:
    if d <= 21:
        print("Gemini")
    else:
        print("Cancer")
elif m==7:
    if d<=22:
        print("Cancer")
    else:
        print("Leo")
elif m==8:
    if d <= 23:
        print("Leo")
    else:
        print("Virgo")
elif m==9:
    if d<=23:
        print("Virgo")
    else:
        print("Libra")
elif m==10:
    if d<=23:
        print("Libra")
    else:
        print("Scorpio")
elif m==11:
    if d<=22:
        print("Scorpio")
    else:
        print("Sagittarius")
elif m==12:
    if d<=21:
        print("Sagittarius")
    else:
        print("Capricorn")