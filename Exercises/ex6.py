user_input = str(input("Enter your string: "))
pal = user_input[::-1]

if user_input == pal:
    print("This string is a palindrome")
else:
    print("This string is not a palindrome")
                 
