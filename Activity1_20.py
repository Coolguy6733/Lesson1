scores = {"Raj": 90, "Sita": 84, "Alex": 76, "Eshaan": 100, "Advik": 89}
total = 0
count = 0
for i in scores.values():
    total = total + i
    count = count+1

average = total/count
print("The average is", average)

print("The least score is",min(scores.values()))
print("The max score is",max(scores.values()))

a = (input("Which student would you like to get? "))

if a in scores:
    print("name found")
else:
    print("name not found")