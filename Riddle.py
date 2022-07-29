category = ["Riddle", "Math"]  # category
choose_category = ""  # for category input
point = 0  # starting point
life = 3  # life amount

print("======================")
print("Welcome To Quiz Game")
print("======================")

while choose_category != "1" or choose_category != "2":  # If user don't choose 1 and 2 ,it's looping
    print("Input Number 1  for 'Riddle' or 2 for 'Math'")
    choose_category = input(">> Input what quiz u want [1 or 2] :")

    if choose_category == "1":  # if user choose 1

        while life != 0:  # question 1 (if the life not aqual to 0)

            # Make it lower and earse the extra space to avoid the 'semilarity answer'->(exp: BARBER,bArBeR) that can be fall
            riddle1 = input(
                "1.I shave every day, but my beard stays the same. What am I? ").lower().strip()

            if riddle1.lower() == "a barber" or riddle1.lower() == "barber":  # If user guess it right
                point += 1  # get 1 point
                print("Your Answer is Right")

                while life != 0:  # question 2
                    riddle2 = input(
                        "2.What goes up but never comes down?").lower().strip()

                    if riddle2.lower() == "a age" or riddle2.lower() == "age":
                        point += 1
                        print("Your Answer is Right")

                        while life != 0:  # question 3 :

                            riddle3 = input(
                                "3.What has words, but never speaks?").lower().strip()

                            if riddle3.lower() == "a book" or riddle3.lower() == "book":
                                point += 1
                                life = 3  # refill the life
                                break

                            else:
                                life -= 1

                            if life == 0:
                                print(
                                    f"You just guessed {point} Riddles, almost perfect!!")  # inform that how much user guess the riddles and how near will finish
                                point -= point
                                break
                    else:
                        life -= 1

                    if point == 3:  # void the bug/looping if user can answer all the riddles
                        break

                    if life == 0:
                        print(
                            f"You just guessed {point} Riddle, unfortunately 2 more riddles!!")
                        point -= point
                        break

            else:  # If user guess it wrong
                life -= 1  # lost one life

            if point == 3:  # if user guess all riddles
                print("Your Answer is Right")
                print("Amazing you guessed all the answer !!\n")
                point -= point  # restart the point
                break

            if life == 0:
                print("Game Over !!!\n")
                life = +3  # refill the life
                break

    elif choose_category == "2":
        while life != 0:  # question 1
            math1 = input(
                "1.If you multiply this number by any other number, the answer will always be the same. What number is this?").lower().strip()

            if math1.lower() == "zero" or math1.lower() == "0":
                point += 1
                print("Your Answer is Right")

                while life != 0:  # question 2
                    math2 = input(
                        "2.If there are 4 apples and you take away 3, how many do you have?").lower().strip()

                    if math2.lower() == "three" or math2.lower() == "3":
                        point += 1
                        print("Your Answer is Right")

                        while life != 0:  # question 3 :

                            mat3 = input(
                                "3.If X is an odd number, when a letter is taken away from X and it becomes even. Which is that number?").lower().strip()

                            if mat3.lower() == "seven" or mat3.lower() == "7":
                                point += 1
                                life = 3
                                break

                            else:
                                life -= 1

                            if life == 0:
                                print(
                                    f"You just guessed {point} Riddles, almost perfect!!")
                                point -= point
                                break
                    else:
                        life -= 1

                    if point == 3:
                        break

                    if life == 0:
                        print(
                            f"You just guessed {point} Riddle, unfortunately 2 more riddles!!")
                        point -= point
                        break

            else:
                life -= 1

            if point == 3:
                print("Your Answer is Right")
                print("Amazing you guessed all the answer !!\n")
                point -= point
                break

            if life == 0:
                print("Game Over !!!\n")
                life = +3
                break

    exit = input("You want continue the game?[Y/N] :").lower().strip()

    if exit.lower() == "yes" or exit.lower() == "y":  # if user input yes or y
        continue
    elif exit.lower() == "no" or exit.lower() == "n":  # if user input no or n
        break
    else:
        # if user input neither yes or no / y or n
        print("HAHAHA IT MEANS YOU PLAY AGAIN !!\n")
        continue

# A smooth sea never made a skilled sailor
