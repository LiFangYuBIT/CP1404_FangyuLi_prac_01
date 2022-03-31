MENU = """1. Show the even numbers from x to y
2. Show the odd numbers from x to y
3. Show the squares from x to y
4. Exit the program"""
print(MENU)
choice = int(input(">>> "))
while choice < 1 or choice > 4:
    print("Invalid choice")
    print(MENU)
    choice = int(input(">>> "))

x = int(input("Enter x: "))
y = int(input("Enter y: "))
if choice == 1:
    for i in range(x, y + 1, 2):
        print(i, end=', ')
    print()
elif choice == 2:
    for i in range(x-1, y, 2):
        print(i, end=', ')
    print()
elif choice == 3:
    for i in range(x, y + 1):
        square = i * i
        print(square, end=', ')
    print()
else:
    print("Finished.")
print(MENU)
choice = int(input(">>> "))

