list_rooz = ["shanbe", "1shanbe", "2shanbe",
             "3shanbe", "4shanbe", "5shanbe", "jome"]
n1 = int(input())
rooz1 = input().split()
n2 = int(input())
rooz2 = input().split()
n3 = int(input())
rooz3 = input().split()
for rooz in rooz1:
    if rooz in list_rooz:
        list_rooz.remove(rooz)
for rooz in rooz2:
    if rooz in list_rooz:
        list_rooz.remove(rooz)
for rooz in rooz3:
    if rooz in list_rooz:
        list_rooz.remove(rooz)

tedad = len(list_rooz)
print(tedad)
