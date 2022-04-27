x = int(input())
for i in range(0,x):
    km = int(input())
    if km % 9 == 0 or km % 11 == 0:
        print("第{0}個點 {1}" .format(i+1,km))