"""
for i in range(1, 21, 2):
    print(i, end=' ')
print()
"""

# a.
for i in range(0, 101, 10):
    print(i, end=' ')
print()

# b.
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# c.
number = int(input("Number of stars: "))
for i in range(0, number):
    star = "*"
    print(star, end='')

# d.
number = int(input("Number of stars: "))
for i in range(0, number+1):
    star = "*" * i
    print(star, sep='')

