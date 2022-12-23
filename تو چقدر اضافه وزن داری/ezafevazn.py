wazn = float(input())
ghad = float(input())
ghad2 = ghad*ghad
bmi = wazn/ghad2
a = "{:.2f}"
c = a.format(bmi)
print(c)
if bmi < 18.50:
    print("Underweight")
if 18.50 <= bmi < 25.00:
    print("Normal")
if 25.00 <= bmi < 30:
    print("Overweight")
if 30 <= bmi:
    print("Obese")
