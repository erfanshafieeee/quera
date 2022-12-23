v = []
x = 1
while x != 0:
    vorodi = int(input())
    if vorodi == 0:
        x = 0
        for i in reversed(v):
            print(i)
    else:
        v.append(vorodi)
