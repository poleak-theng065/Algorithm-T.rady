text = "9394884039"
# Question 1
count8 = 0
for i in range(len(text)):
    if text[i] == "8":
        count8 += 1
print("Numbebr 8 have ",count8)
# Question 2
first8 = False
for i in range(len(text)):
    if text[i]=="8" and not first8:
        print("Idext first 8 is",i)
        first8 = True