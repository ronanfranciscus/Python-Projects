import random   # Method to get a random name (can be use for number too)

lists = []      # empty list  (in python, array is called list)
number = 1      # list number (at line 31)
convince = " "  # To convince a user to get ready for the result (at line 46)
no = "No"       # if user type 'No', the program is end (at line 59)
countdown = 3   # to count down before get ther result (at line 53)
list = 1        # To know, how much cointain that u already input(at line 20)

# welcome greeting
print("-"*21)
print("Welcome To Picker App")
print("-"*21)

# input how much quantity of list you want
quantities = int(input(">> Put how much quantitiy you want : "))

# input a contain for list
for q in range(quantities):  # amount of input / list depends with how much quantity you put
    add = input(f">> Input list {list}: ")  # {list} -> number list input
    # this is adding a contain of list (input first, get the first postion of list)
    add = lists.append(add)
    list += 1  # add amount of list

print("-"*20)
print("here your list :")

# this is print a list that already appended
for l in lists:
    print(f"{number}.{l}")
    number += 1  # number of list
print("")

# This can be anything depends on what u need, feel free to change
print("WHO GET $100K TODAY ?")

# This gonna pick a random content in a list
choose = random.choice(lists)

# Check that you are ready to get the result
# if convince not equal to "No" will give the input
while convince.upper() != no.upper():
    # This input use method .upper() and .strip() to avoid a "false semilarity answer"
    # False semilarity answer -> ("nO","no","(with space)no","YeS",ect)
    # So these method upper()= for make input uppercase and strip()= to remove a extra space
    convince = input(">> Are you ready ?(Yes/No):").upper().strip()
    print("")
    if convince.upper() != "YES" and convince.upper() != no.upper():  # if your answer neither "yes" or "no"
        continue  # back to input until your answer either "yes" or "no"

    if convince.upper() == "YES" :  # if your answer is "yes"
        print("Let's Count down :")
        while countdown != 0:  # count down to get a result
            print(countdown)
            countdown -= 1
        print(f"CONGRATULATION {choose} !! YOU ARE THE CHOOSEN ONE")  # result
        break  # program stop

    if convince.upper() == no.upper():  # if your answer is "No"
        break  # program stop
       
