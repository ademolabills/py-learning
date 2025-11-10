set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
p = set1.union(set2)
set1.update(set2)


set1.add("orange")
set1.remove("c")

print(set1)

x = frozenset({"apple", "banana", "cherry"})
y = frozenset({"bmw", "benz"})
z = x.union(y)

print(z)

# x.add("orange")  #@ This will raise an AttributeError
print(x)
print(type(x))