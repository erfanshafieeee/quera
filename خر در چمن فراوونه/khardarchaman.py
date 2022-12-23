a, b, l = map(int, input().split())
sum = 0
for i in range(l):
    if i % 2 == 0:
        sum = sum+a
    else:
        sum = sum+b
print(sum)
