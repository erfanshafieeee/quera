n = int(input())
x = input().split()
max=0
for i in x:
    i=int(i)
    if i>=max:
        max=i
print(max)
