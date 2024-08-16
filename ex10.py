combo = ''
for i in range(5):
    user_input = input("Enter Number: ")
    combo += str(user_input)
min = combo[0]
max = combo[0]
for i in range(len(combo)):
    if combo[i]>max:
        max = combo[i]
    if combo[i] < min:
        min = combo[i]
print("Max:",max,"and Mini:",min)