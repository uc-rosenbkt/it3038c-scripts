operation = input('''Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
Enter here: ''')

number_1 = int(input('Enter your first number: '))
number_2 = int(input('Enter your second number: '))

#Addition
if operation == '+':
    print('{} + {} = '.format(number_1, number_2))
    print(number_1 + number_2)

#Subtraction
elif operation == '-':
    print('{} + {} = '.format(number_1, number_2))
    print(number_1 - number_2)

#Multiplication
elif operation == '*':
    print('{} + {} = '.format(number_1, number_2))
    print(number_1 * number_2)

#Division
elif operation == '/':
    print('{} + {} = '.format(number_1, number_2))
    print(number_1 / number_2)

else:
    print('You have not entered a valid value, please run the program again')