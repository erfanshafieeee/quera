a = int(input())
b = int(input())
c = int(input())
d = int(input())
sum = a+b+c+d
Average = sum/4
Product = a*b*c*d
max = max([a, b, c, d])
min = min([a, b, c, d])
ragham = "{:.6f}"
sum = ragham.format(sum)
Average = ragham.format(Average)
Product = ragham.format(Product)
max = ragham.format(max)
min = ragham.format(min)
print(
    f"Sum : {sum}\nAverage : {Average}\nProduct : {Product}\nMAX : {max}\nMIN : {min}")
