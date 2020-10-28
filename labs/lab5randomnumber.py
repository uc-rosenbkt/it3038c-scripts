import random
random_number = random.randint(1,1000)
win = False
turns = 0
while win == False:
    your_guess = input("Enter a number between 1 and 1,000 ")
    turns += 1
    if random_number==int(your_guess):
        print("Winner!")
        print("Number of turns you have used: ",turns)
        win == True
        break
    else:
        if random_number > int(your_guess):
            print("Your guess was low, please enter a higher number.")
        else:
            print("Your guess was high, please enter a lower number.")