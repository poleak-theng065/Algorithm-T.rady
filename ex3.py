user_input = input("Input text: ")
isCapital = False
for i in range(len(user_input)):
    if user_input[i]==user_input[i].upper():
        isCapital = True
if isCapital:
    print("Yes,We have capital!")
else:
    print("No, We don't have capital!")