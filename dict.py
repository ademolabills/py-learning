students = {
	"name": "Funmbi",
	"age": 100,
	"class": "Python",
	"hubby": "reading",
	"favourite_food": ["Eba", "Fufu", "Rice"],
	"extra_details": {
		"last_name": "Funmbi",
		"email": "Funmbi@gamil.com",
	},
    "likes": ("coding", "teaching", "learning"),
    "dislikes": {"laziness", "procrastination"}
}

print(students["name"])
print(students["favourite_food"][2])
print(students.get("age"))
# print(students["extra_details"]["email"])
# print(students.get("extra_details").get("last_name"))

print("\n")

print(students.get("middle_name"))  #@ This will return None
# print(students["middle_name"])  #@ This will raise a KeyError
print(students.get("middle_name", "Not Found"))  #@ This will return "Not Found"

print(students["likes"])


#@ dict methods
print("\n")
print(students.keys())
print("\n")
print(students.values())

print("\n")
# print(students["extra_details"].values())

print("\n")
print(students.items())

students.update({"class": students["class"] + " JavaScript, HTML, CSS"})
print(students)
print("\n")

print("\n")
student_copy = students.copy()
student_copy.update({"name": "Adeola", "age": 25})
student_copy.update({"height": "5'4"})


print(student_copy)

student_copy.pop("dislikes")
student_copy.popitem()  #@ removes the last inserted item
students.setdefault("Country", "Nigeria")  #@ adds the key with the specified value if the key is not already present

print(f"\nstudents dict after pop and setdefault: \n {students} \n")

print("\n")
print(student_copy)
