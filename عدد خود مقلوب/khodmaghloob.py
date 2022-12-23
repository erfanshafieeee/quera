x=input()
x=int(x)
x1=x
y=0
while x1>0:
    y=y*10+x1%10
    x1=x1//10
if x==y:
    print("YES")
else:
    print("NO")
