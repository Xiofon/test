x = int(input(""))
for i in range(0,x):
    nu = []
    ans = 0
    for a in range(0,4):
        nu.append(int(input("")))
    if nu[2] - nu[1] == nu[3] - nu[2]:
        for a in range(0,4):
            print(nu[a],end=" ")
        ans = nu[3]+(nu[3]-nu[2])
        print(ans)
        print("此為等差數列")
    elif nu[2] / nu[1] == nu[3] / nu[2]:
        for a in range(0,4):
            print(nu[a],end=" ")
        ans = nu[3]*(nu[3]/nu[2])
        print(ans)
        print("此為等比數列")