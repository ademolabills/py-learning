# a, b, c = 5, 3, 8

# if (a + b * 2) ** 2 // 5 % 3 == 1 and not b > a or c // 2 + a % b * 3 <= 10:
    
#     a += b if c % 2 == 1 else c - b
#     print("Branch 1:", a, b, c)
# else:
    
#     b = (a * c) // (b + 1) - 4
#     print("Branch 2:", a, b, c)



x, y, z = 7, 4, 10

if x ** 2 // 5 + y * 3 % 4 > z // 2:
    if not (y + z // 3 == x or x % y > 2 and z - x * 2 < 0):
        x = x + y if z % 2 == 0 else y - z
        print("Inner If:", x, y, z)
    else:
        y += (x * 2) // (z % 5 + 1)
        print("Inner Else:", x, y, z)
else:
    if x + y * z % 3 == 0 or not (z // y < x and y ** 2 > 10):
        z -= x if y % 2 else y + 1
        print("Outer Else If:", x, y, z)
    else:
        x, y, z = y, z, x
        print("Outer Else Else:", x, y, z)
