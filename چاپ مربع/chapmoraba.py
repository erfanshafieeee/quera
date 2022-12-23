x = int(input())
print("*" * x)
for i in range(x-2):
    print("*", end="")
    print(" " * (x-2), end="")
    print("*")
print("*" * x)
