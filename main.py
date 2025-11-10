"""
1. Given:
```python
nums = [3, 6, 9, 12]
```
- Use a method to remove the number `9`.
- Use a method to add `15` to the list.
"""

nums = [3, 6, 9, 12]
nums.remove(9)
nums.append(15)

print(nums)  # Output should be [3, 6, 12, 15]

"""
2. **Write a Python statement to:**
- Create a **tuple** called `colors` containing `"red", "green", "blue"`.
- Access and print the first color.
"""

colors = ("red", "green", "blue")
print(colors[0])  # Output should be "red"


"""
- Print only the keys.
- Print only the values.
- Change the age to 19.
"""

student = {
    "name": "Tolu",
    "age": 18,
    "grade": "A"
}

print(student.keys())
print(student.values())
student["age"] = 19
student.update({"age": 19})

print(student)  # Output should show age as 19

a = {1, 2, 3, 4}
b = {1, 3, 4, 5, 6}

print(a.union(b)) #@ Output: {1, 2, 3, 4, 5, 6}

#! Find their intersection.
print(a.intersection(b)) #@ Output: {1, 3, 4}

#Find the difference between `a` and `b`.
# explanation: The difference between two sets `a` and `b` (i.e., `a - b`) is a set containing elements that are in `a` but not in `b`.
new_set = a.difference(b)
print(new_set)
print(b.difference(a))

# Find the items that are not in both sets.
print(a.symmetric_difference(b))  #@ Output: {2, 5, 6}