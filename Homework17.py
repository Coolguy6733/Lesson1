a = int(input("How many sandwiches did they buy,\n1 sandwich = $2: "))
b = a*2
print("The total is", b)
c = int(input("How much did the customer pay? "))
d = c-b
if c >= b:
    print("The change is", d)
else:
    print("The customer did not pay enough")