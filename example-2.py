set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
p = set1.union(set2)
print(p)
set1.update(set2)
print(set1) 

set3 = {"APTech", "NIIT", "Alt_School", "apple"}
set4 = {"google", "microsoft", "apple"}

# set5 = set3.intersection(set4)
set5 = set3 & set4
print(set5) 


set6 = {"apple", "banana", "cherry"}
set7 = {"google", "microsoft", "apple"}

set6.intersection_update(set7)
print(set6) 


set8 = {"apple", "banana", "cherry"}
set9 = {"google", "microsoft", "apple"}
set10 = set9.difference(set8)
set11 = set8 - set9
print(set10)
print(set11)