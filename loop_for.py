fruits = ["apple", "banana", "cherry"]

# for fruit in fruits:
    
#     if fruit == "banana":
#         fruit = fruit.upper()
#         print(f"{fruit} are my favorite!")
#         break
    
#     print("I like", fruit)

search_list = ["apple", "banana", "kiwi"]
search_fruit = input("Enter a fruit to search for: ")

for fruit in search_list:
    if fruit == search_fruit:
        print(f"Found the fruit: {search_fruit}")
        break
else:  # <--- This block runs ONLY because the 'break' was NOT hit
    print(f"**FAILURE:** Could not find {search_fruit} in the list.")


# Print only the even numbers in a range
print("Only showing even numbers:")
for number in range(1, 7):
    
    if number % 2 != 0:
        continue  # <--- Skips the print statement below for odd numbers
    
    print(f"Found an even number: {number}")