x1, y1, x2, y2 = map(int, input().split())
no = 0
if x1 == x2:
    print("Vertical")
else:
    no = no+1
if y1 == y2:
    print("Horizontal")
else:
    no = no+1
if no == 2:
    print("Try again")
