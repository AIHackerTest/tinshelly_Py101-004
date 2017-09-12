import random

correct_number = random.randint (0,20)

i = 0
while i < 10:
    print ("Pls input an integral number between 0 and 20: ", end = ' ')
    input_number = int(input())
    if input_number == correct_number:
        print ("Congratulations! You are correct!")
        exit (0)

    elif input_number < correct_number:
        print ("It's too small.")

    else:
        print ("Is's too large.")

    chances_left = 9 - i
    if chances_left == 0:
        print ("Sorry, no chance left.")
    else:
        print (f"You still have {chances_left} chances.")
    i = i + 1
