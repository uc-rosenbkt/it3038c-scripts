print("Please type 'your name'")

###you can take this and put it in your nameage file in place of myname = input()
myName = input()
while myName != 'Keith':
    if myName == 'your name':
        print("That is a lame joke...")
    else:
        print('What is your real name?')
    myName = input()



###stop here

print("Hello " + myName + ". Haha.")