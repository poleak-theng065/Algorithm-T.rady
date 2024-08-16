number = "454639"
# Question 1
countODD = 0
countEVEN = 0
for i in range(len(number)):
    if int(number[i]) % 2 == 1:
        countODD += 1
    else: 
        countEVEN += 1
print("Count ODD:",countODD)
print("Count Even:",countEVEN)
# Question 2
sum = 0
for i in range(len(number)):
    sum += int(number[i])
print("Sum: ",sum)
# Question 3
sumEven = 0
for i in range(len(number)):
    if int(number[i]) % 2 == 0:
        sumEven += int(number[i])
print("Sum Even: ",sumEven)
# Question 4
reverse_print = ""
for i in range (len(number)):
    reverse_print = reverse_print + number[len(number)-1-i]
print("Answer:",reverse_print)