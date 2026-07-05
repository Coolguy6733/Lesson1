numbers = [1, 2, 3, 4, 5, 6]

even = [x for x in numbers if x%2==0]
odd = [x for x in numbers if x%2!=0]

print("Even numbers of list:", even)
print("Odd numbers from list:", odd)

fruits = ['apple', 'banana', 'strawberry',' orange']

capital = [fruit.capitalize()for fruit in fruits]

print(capital)