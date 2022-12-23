a, b = map(int, input().split())
if b > 10:
    print("Left", end=" ")
else:
    print("Right", end=" ")
cheghadr = (10-a)+1
if b > 10:
    kodom = (20-b)+1
else:
    kodom = 20-(20-b)
print(cheghadr, kodom)
