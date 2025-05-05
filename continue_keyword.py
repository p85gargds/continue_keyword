#taking input from user
var = int(input("Please enter a number(greater than 6):"))
while var > 0:
    var = var - 1
    if var == 5:
        continue
    print("\n current variable value:",var)
print("\n goodbye")