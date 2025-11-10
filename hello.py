a, b, c = 3, 4, 9
d, e, f = 8, 8, 1
g = h = i = 7

#@ this is a list
fruits = ["apple", "banana", "cherry", ("Ford", "BMW", "Volvo")]
j, k, l, m = fruits

print(fruits[0])
print(fruits[2])
fruits[2] = "orange"
fruits.append("Mango")
print(fruits[2])
print(fruits[3])
print(fruits)

#@ data type: tuple
cars = ("Ford", "BMW", "Volvo", ("Toyota", "Benz", "Honda"))
print(cars[0])
print(cars[2])
cars[2] = "Audi"  #@ This will raise an error because tuples are immutable
cars.append("Mazda")  #@ This will also raise an error
print(cars[3])
print(cars)

# print(j)
# print(k)
# print(l)

# print(g + h + i)
# print(d)
# print(e)
# print(f)