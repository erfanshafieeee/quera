
tedad = input()
tedad = int(tedad)
x = tedad
y = tedad
for i in range(1, x+1):
    for j in range(1, y+1):
        print(format(i*j), end=' ')
    print()
