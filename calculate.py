print("Do you want to : add(1), subtract(2), multiply(3) or divide(4)?")
activity = int(input("Enter the activity number : "))
number1 = int(input("The first number : "))
number2 = int(input("The second number : "))

if activity == 1:
    final = number1 + number2
    print("Your result is ")
    print(final)

if activity == 2:
    final = number1 - number2
    print("Your result is ")
    print(final)

if activity == 3:
    final = number1 * number2
    print("Your result is ")
    print(final)

if activity == 4:
    final = number1 / number2
    print("Your result is ")
    print(final)