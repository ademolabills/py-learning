fruits = ["apple", "banana", "cherry", "apple", "cherry"] #@ lIST
tubber = ["Yam", "Potato", "Carrot"]
veggies = ("Tomato", "Cucumber", "Onion")

fruits_tubber = fruits + tubber
fruits_tubber.append("Mango")
fruits_tubber.extend(veggies)
print(fruits_tubber)




my_fruits =     ("apple", "banana", "cherry", "apple", "cherry") #@ TUPLE
some_fruits =   {"apple", "banana", "cherry", 6, ("apple", "banana")}  #@ SET

cars = set(("toyota", "bmw", "benz"))  #@ SET from string
print(cars)

some_fruits.add("Mango")
cars.add("venza")
cars.remove("toyota")
print(cars)

y = (15, 11, 1)
fruit_cars = some_fruits.union(cars)
fruit_cars1 = fruit_cars.union(y)
fruit_cars2 = fruit_cars.update(cars)
print(fruit_cars2)

# for item in fruit_cars:
#     print(item) 

# print(0 in some_fruits) 

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}

# set3 = set1.intersection(set2)
# print(set3) 

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}

# set3 = set1.intersection(set2)
# print(set3)


# print(fruits)
# print(my_fruits)
# print(some_fruits)