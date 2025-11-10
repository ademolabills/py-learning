# day = 4

# #@ INPUT
# day = input("Please Enter a day (1-7): ")


# match day:
#     case 1.0:
#         print("Monday")
#     case 2.0:
#         print("Tuesday")
#     case 3.0:
#         print("Wednesday")
#     case 4.0:
#         print("Thursday")
#     case 5.0:
#         print("Friday")
#     case "6.0":
#         print("Saturday")
#     case 7.0:
#         print("Sunday")
#     case _:
#         print("Invalid day! Please enter a number between 1 and 7.")


# # Calculator

# input1 = int(input("Enter first number: "))
# operator = input("Enter operator (+, -, *, /): ")
# input2 = float(input("Enter second number: "))

# match operator:
#     case "+":
#         print(f"{input1} + {input2} = {input1 + input2}")
#     case "-":
#         print(f"{input1} - {input2} = {input1 - input2}")
#     case "*":
#         print(f"{input1} * {input2} = {input1 * input2}")
#     case "/":
#         print(f"{input1} / {input2} = {input1 / input2}")
#     case _:
#         print("Invalid operator! Please enter one of (+, -, *, /).")


# Why Match Case over If-Else?
# Using match-case can enhance code readability and organization, especially when dealing with multiple discrete values or conditions.

# It provides a clear structure for handling different cases, making it easier to understand the flow of logic at a glance.

# Additionally, match-case can be more efficient in certain scenarios, as it can optimize the evaluation of cases compared to multiple if-else statements.


#@ IF ELSE
#@ Operators
#@ Precedence of Operators

# a = int(input("Enter first number: "))
# operator = input("Enter operator (+, -, *, /): ")
# b = float(input("Enter second number: "))

# #@ Using if else statements
# if operator == "+":
#     print(f"{a} + {b} = {a + b}")
# elif operator == "-":
#     print(f"{a} - {b} = {a - b}")
# elif operator == "*":
#     print(f"{a} * {b} = {a * b}")
# elif operator == "/":
#     print(f"{a} / {b} = {a / b}")
# else:
#     print("Invalid operator! Please enter one of (+, -, *, /).")
    
    
#@ OPERATORS
#@ Arithmetic Operators: +, -, *, /, %, **, //
#@ Comparison Operators: ==, !=, >, <, >=, <=  
#@ Assignment Operators: =, +=, -=, *=, /=, %= 
#@ Logical Operators: and, or, not

y = 20
z = 3

print("Arithmetic Operators:")
print(f"{y} ** {z} = {y ** z}")
print(f"{y} // {z} = {y // z}")
print(f"{y} % {z} = {y % z}")
print(f"{y} + {z} = {y + z}")
print(f"{y} - {z} = {y - z}")
print(f"{y} * {z} = {y * z}")
print(f"{y} / {z} = {y / z}")


#@ Comparison Operators
print("\nComparison Operators:")
print(f"{y} == {z}: {y == z}")
print(f"{y} != {z}: {y != z}")
print(f"{y} > {z}: {y > z}")
print(f"{y} < {z}: {y < z}")
print(f"{y} >= {z}: {y >= z}")
print(f"{y} <= {z}: {y <= z}")

#@ Assignment Operators
print("\nAssignment Operators:")
a = y
b = z
print(f"a = {a}")
print(f"b = {b}")

a += b
print(a)

a -= b
print(a)

b *= 2
print(b)


if b != 0:
    a /= b
    print(a)

c = 10
d = 3
check = d + c and c > d or d == 6 and c < 10
print(f"check: {check}")

check2 = (c > d) and (c <= d) or not (d == 3) and (5 + 10) * 2 > 20
check2 = True and False or not True and True
check2 = True and False or False and True
check2 = False or False
print(f"check2: {check2}")


equ1 = 1 + 2 * 3 ** 2 // 4 - 5 % 2

equ2 = 1 + 2 * 3 ** 2 // (4 - 5 % 2)

equ3 = 1 + 2 * (3 ** 2) // (4 - 5 % 2)

equ4 = 1 + 2 * (3 ** 2) // (4 - 5 % 2) ** 2

l, m, n = 5, 3, 8
check3 =  ("i" in "india") and (l > n) or ("a" not in "apple") and l % 2 != 0 or (10 // m == 3) and n is 15
# check3 =  True and False or False and l % 2 != 0 or True and n is 15
# check3 =  True and False or False and 1 != 0 or True and n is 15
# check3 =  True and False or False and True or True and n is 15
# check3 =  True and False or False and True or True and False
# check3 =  False or False or False
# check3 =  False

if check3:
    print("check3 is True")
else:
    print("check3 is False")
