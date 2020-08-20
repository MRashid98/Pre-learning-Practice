player_a = str(input("Player A Name: "))
player_b = str(input("Player B Name: "))

new_game = 'y'

def compare(a,b):
    if a == b:
        print("Tie")
    elif a == 'R':
        if b == 'P':
            print(player_b, "wins")
        else:
            print(player_a, "wins")
    elif a == 'P':
        if b == 'S':
            print(player_b, "wins")
        else:
            print(player_a, "wins")
    elif a == 'S':
        if b == 'R':
            print(player_b, "wins")
        else:
            print(player_a, "wins")
    else:
        print("Invalid Input")

print("To enter your choice simply enter the initial in capital")
print("e.g. For Rock enter R")


while new_game == 'y':
    a_choice = str(input(player_a + " enter your choice: "))
    b_choice = str(input(player_b + " enter your choice: "))
    compare(a_choice,b_choice)
    new_game = str(input("Want to start a new game? y/n "))


print("Thanks for playing")

