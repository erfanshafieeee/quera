a, b, c = map(int, input().split())
if a == 0 or b == 0 or c == 0:
    print("No")
else:
    if a+b+c == 180:
        print("Yes")
    else:
        print("No")
