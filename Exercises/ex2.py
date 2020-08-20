number = int(input("Enter a number: "))
if number % 2 == 0:
    if number % 4 == 0:
        print("Your number is a multiple of four")
    else:
        print("Your number is even")
else:
    print("Your number is odd")


num = int(input("Enter first number: "))
check = int(input("Enter second number: "))

if num % check == 0:
    print("Numbers devide evenly")
else:
    print("Numbers dont divide evenly")
