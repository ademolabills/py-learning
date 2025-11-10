count = 0

# The loop keeps running as long as 'count' is less than 5.
# while count < 10:
#     print(f"Count is: {count}")
    
#     if count == 3:
#         break
    
#     count += 1  # This line is critical to eventually stop the loop!
    

# while count < 5:
#     count += 1
    
#     if count == 3:
#         continue
    
#     print(f"Count is: {count}")
    

import random

random_count = random.randint(1, 10)
print(random_count)
while random_count > 0:
    print(f"Random count is: {random_count}")
    
    if random_count == 5:
        print("Hit the magic number 5, stopping early!")
        break
    
    random_count -= 1


magic_num = random.randint(1, 10)
max_attempts = 3
attempts = 0

while attempts < max_attempts:
    user_guess = int(input("Guess the number (between 1 and 10): "))
    
    if user_guess == magic_num:
        print("Congratulations! You've guessed the number!")
        break
    
    print("Wrong guess, try again.")
    attempts += 1
else:
    print("Sorry, you've used all your attempts. The magic number was:", magic_num)