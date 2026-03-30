print("Enter Marks Obtained in 5 Subjects: ")
math = int(input("maths: "))
english = int(input("english: "))
science = int(input("science: "))
history = int(input("history: "))
pe = int(input("P.E.: "))

sum = math+english+science+history+pe
print("sum of all the subject marks =", sum)

perc = (sum/500)*100

print(end="Percentage Mark = ")
print(perc)