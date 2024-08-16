string = "3 4 5 6"
# Question 1
number = ''
for i in range (len(string)):
    if string[i]!= " ":
        number += string[i]
print("Result:",number)
# Question 2
result = ''
multiply = 2
for i in range (len(string)):
    if string[i]!=" ":
        multiply *= int(string[i])
        result += str(multiply)
        multiply = 2
    else:
        result += string[i]
print("Result2:",result)