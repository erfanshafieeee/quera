x = int(input())
sum = 0
for i in range(x):
    if i > 0:
        if x % i == 0:
            i = int(i)
            sum = sum+i

if x == sum:
    print("YES")
else:
    print("NO")
