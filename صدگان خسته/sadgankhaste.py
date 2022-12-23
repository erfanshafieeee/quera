def maghloob(number):
    y = 0
    while number > 0:
        y = y*10+number % 10
        number = number//10
    return (y)


add1 = int(input())
add2 = int(input())

add11 = maghloob(add1)
add22 = maghloob(add2)

if add11 > add22:
    print(f"{add2} < {add1}")


if add22 > add11:
    print(f"{add1} < {add2}")

if add1 == add2:
    print(f"{add1} = {add2}")
