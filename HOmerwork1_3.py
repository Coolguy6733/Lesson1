age = int(input("Enter your age: "))
year = int(input("Enter the year you were born: "))

if 2026 - year == age:
    if age % 2 == 0:
        print("Your age is correct and even")
    else:
        print("Your age is correct and odd")
else:
    print("Your age is incorrect")