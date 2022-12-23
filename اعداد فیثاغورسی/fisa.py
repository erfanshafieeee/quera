zel1 = input()
zel1 = float(zel1)
zel2 = input()
zel2 = float(zel2)
zel3 = input()
zel3 = float(zel3)
if zel1 > zel2 and zel1 > zel3:
    if zel1*zel1 == zel2*zel2 + zel3*zel3:
        print("YES")
    else:
        print("NO")
if zel2 > zel1 and zel2 > zel3:
    if zel2*zel2 == zel1*zel1 + zel3*zel3:
        print("YES")
    else:
        print("NO")
if zel3 > zel2 and zel3 > zel1:
    if zel3*zel3 == zel2*zel2 + zel1*zel1:
        print("YES")
    else:
        print("NO")
