name = str(input("What's your name? "))
age = int(input("How old are you? "))
bday = str(input("Have you had your birthday yet? (y/n) "))

 
if bday == 'n':
    age += 1 
elif bday == 'y':
    age = age


year = (100 - age) + 2020
print(name + ", you will turn 100 in the year", year)
           
times = int(input("Enter another number: "))

for i in range(times):
    print(name + ", you will turn 100 in the year", year)
