tup1 = (5, 8, 1, 2)
tup2 = (6, 7, 1, 2)

result = tuple(x*y for x, y in zip(tup1, tup2))
print("Element-wise Result:", result)