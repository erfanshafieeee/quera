x=input()
x=int(x)
n=input()
n=int(n)
if n==0:
    x=20
if n==7:
    x=x
if 1<=n<=6 or 8<=n:
    x=x-n
if x<=0:
    x=0
print(x)