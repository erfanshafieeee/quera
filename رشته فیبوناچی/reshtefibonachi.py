n = int(input())

fibo = [1, 1]
for i in range(2, 11):
    fibo.append(fibo[i - 2] + fibo[i - 1])

keeper = []
for i in range(1, n + 1):
    if i in fibo:
        keeper.append("+")
    else:
        keeper.append("-")

print("".join(keeper))