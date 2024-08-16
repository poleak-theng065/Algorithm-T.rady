# Question3
numbers = "3 4 5 6"
result = ""
for i in range(len(numbers)):
    if numbers[i] != " ":
        result+=numbers[i]
print(result)
# Question2
sum = 0
for i in range(len(numbers)):
    if numbers[i] != " ":
        sum += int(numbers[i])
print(sum)

