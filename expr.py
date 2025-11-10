a = int(input("Enter a number for a: "))
b = int(input("Enter a number for b: "))
c = int(input("Enter a number for c: "))

expr = (a ** 2 + b * 3 - c // 2) % (b + 1) + (c > a * 2) * (a - b)

if (expr % 2) == 0 and expr > (b + c):
    print("High even expression!")
elif (expr % 2 ) != 0 and expr < (a * b):
    print("Low odd expression!")
else:
    print("Balanced expression!")