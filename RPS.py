# Rock,Paper,Scissor game
import random  # module to get random pick

rps = ("Rock", "Paper", "Scissor")  # Computer choices
rps = random.choice(rps)  # random choice from list of rps

print("-"*38)
print("Welcome To the Rock,Paper,Scissor Game")
print("-"*38)

while True:  # passing true

    # using method title() and strip() to avoid the 'semilarity answer' that can be false
    # input Rock or Paper or Scissor
    user = input(">>Choose [Rock,Paper,Scissor]: ").title().strip()

    # if user input like in a list of rds
    if user.title() == "Rock".title() or user.title() == "Paper".title() or user.title() == "Scissor".title():
        print(f"You are -{user}-")
        print(f"Your oponen are -{rps}-")

        if user == rps:  # if user input like rps random choice
            print(f"You draw because both of you are {rps}")

        # If Condition for user input and rps random choice
        elif user == "Paper":
            if rps == "Rock":
                print("You win 'Paper cover a Rock'")
            else:
                print("You lose 'Scissor cut a Paper'")

        elif user == "Rock":
            if rps == "Scissor":
                print("You win 'Rock break the Scissor'")
            else:
                print("You lose 'Paper cover a Rock'")

        elif user == "Scissor":
            if rps == "Paper":
                print("You win 'Scissor cut a Paper'")
            else:
                print("You lose 'Rock break the Scissor'")

    # To convince user for continue the game or not
    exit = input("You want Exit the game ?[Yes/No] ").title().strip()

    if exit.title() == "yes".title():  # if user type yes
        break  # system stop


# Fortis Fortuna Adiuvat
