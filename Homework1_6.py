test_dict = {"Humans": 3, "rule": 3, "the": 3, "world": 2}

print("The original dictionary:"+ str(test_dict))
K=2

res=0
for key in test_dict:
    if test_dict[key] == K:
        res = res+1

print("Frequency of K is :", str(res))