import time

start_time = time.time()
###comment
print("What is your name?")
myName = input()
print("Hello " + myName + ". That is a good name. How old are you?")
myAge = int(input())

if myAge < 13:
    print("You're not even a teenager yet!")
elif myAge == 13:
    print("You're a teenager now...yay...")
elif myAge > 13 and myAge < 30:
    print("You're young and dumb")
elif myAge >= 30 and myAge < 65:
    print("You're adulting...")
else:
    print("... and you're not dead yet?")

###set the program age before giving it to the use
programAge = int(time.time() - start_time)

print("%s? That's funny, I'm only %s seconds old." % (myAge, programAge))
print("I wish I was %s years old" % (myAge * 2))
time.sleep(2)
print("I'm tired. I'm done. Goodnight.")