num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))
op = str(input("enter operator (=, -, *): "))
if op == "+":
    result = num1 + num2
elif op == "-":
    result = num1 - num2
elif op == "*":
    result = num1 * num2

print(str(num1) + " " + op + " " + str(num2) + " = " + str(result))
