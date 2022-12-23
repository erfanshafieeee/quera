add = input()
add = int(add)
result = 0
while add > 0:
    baghi = add % 10
    result = result+baghi
    add = add//10
    if result > 9 and add == 0:
        add = result
        result = 0
