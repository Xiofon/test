x = int(input("X軸座標:"))
y = int(input("Y軸座標:"))
ans = x ** 2 + y ** 2
if (x == 0) and (y == 0):
    print("該點位於原點")
elif (x == 0) and (y > 0):
    print("該點位於上半平面Y軸上,離原點為根號{0}".format(ans))
elif (x == 0) and (y < 0):
    print("該點位於下半平面Y軸上,離原點為根號{0}".format(ans))
elif (y == 0) and (x > 0):
    print("該點位於右半平面X軸上,離原點為根號{0}".format(ans))
elif (y == 0) and (x < 0):
    print("該點位於左半平面X軸上,離原點為根號{0}".format(ans))
elif (x > 0) and (y > 0):
    print("該點位於第一象限,離原點為根號{0}".format(ans))
elif (x < 0) and (y > 0):
    print("該點位於第二象限,離原點為根號{0}".format(ans))
elif (x < 0) and (y < 0):
    print("該點位於第三象限,離原點為根號{0}".format(ans))
elif (x > 0) and (y < 0):
    print("該點位於第四象限,離原點為根號{0}".format(ans))
