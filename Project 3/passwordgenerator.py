# Random module is used to perform the random generations
import random
# String module contains different string constants for each generator 
import string
# This operation prompts the user to enter a number for the password generator they want
operation = input('''Welcome to the multi-password generator. Please select which type of 10 character password you want:
1 for lowercase letters
2 for uppercase and lowercase letters
3 for letters and numbers
4 for letters, numbers, and special characters
Enter here: ''')
# Script for lowercase password 
if operation == '1':
    def get_random_string(length):
        # Uses string constant string.ascii_lowercase to use all lowercase letters
        letters = string.ascii_lowercase
        # random.choice picks a character from the constant and join adds each character to the string after each iteration
        result_str = ''.join(random.choice(letters) for i in range(length))
        print("Random lowercase letters password is:", result_str)
        # Looped 10 times
    get_random_string(10)
# Script for uppercase and lowercase letters
elif operation == '2':
    def get_random_string(length):
        # Uses constant string.ascii_letters for combonation of uppercase and lowercase
        letters = string.ascii_letters
        result_str = ''.join(random.choice(letters) for i in range(length))
        print("Random letters password is:", result_str)
        # Looped 10 times
    get_random_string(10)
# Script for letters and numbers
elif operation == '3':
    def get_random_alphanumeric_string(length):
        # Uses constants string.ascii_letters and string.digits to get numbers and uppercase/lowercase letters
        letters_and_digits = string.ascii_letters + string.digits
        result_str = ''.join(random.choice(letters_and_digits) for i in range(length))
        print("Random alphanumeric password is:", result_str)
        # Looped 10 times
    get_random_alphanumeric_string(10)
# Script for letters, numbers, and special characters
elif operation == '4':
    def get_random_password_string(length):
        # Uses constants string.ascii_letters, string.digits, and string.punctuation to get numbers, uppercase/lowercase letters, and special characters
        password_characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(password_characters) for i in range(length))
        print("Random alphanumeric/special characters password is:", password)
        # Looped 10 times
    get_random_password_string(10)
# If you do not enter a number 1-4 you will get this
else:
    print('You have not entered a valid value, please run the program again')
