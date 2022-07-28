life = 0             # life that u have
secret_number = 10   # Number that u must guess(feel free to change)
ready = " "          # Convince the user 'yes' or 'no


print("-"*14)
print("Guess A Number")
print("-"*14)
print("Type 'No' to exit the game")
print("")

while ready.upper() != "No".upper():  # if user not type 'No' -> continue the input
    ready = input("Are you ready ?[Yes/No] ").upper().strip()

    if ready.upper() == "Yes".upper():  # if user not type 'Yess'
        while life <= 3:  # user attemp not more than 3 times
            guess = int(input(">> Guess The Number : "))  # guess the number
            life += 1  # add +1 in life

            if guess == secret_number:  # if user input equal to 'secret_number'
                print("Amazing you guessed the number !!")
                life -= life   # reset to 0
                break  # program stop

            if life == 3:  # if user attemp equal to 3 times
                print("Game Over")
                life -= life  # reset to 0
                break  # program stop


# Have a nice day everyone !!!
