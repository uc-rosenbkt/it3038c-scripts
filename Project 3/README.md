# Project 3
This project allows the user to select a password generator
### Random needs to be imported to perform random generations and string is imported for the constants used in each generator
```
import random
import string
```
### This operation welcomes the user and prompts them to enter a number 1-4 for the password they would like generated
```
operation = input('''Welcome to the multi-password generator. Please select which type of 10 character password you want:
1 for lowercase letters
2 for uppercase and lowercase letters
3 for letters and numbers
4 for letters, numbers, and special characters
Enter here: ''')
```
### This is the first operation for generating a password with all lowercase letters
```
if operation == '1':
    def get_random_string(length):
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(length))
        print("Random lowercase letters password is:", result_str)
    get_random_string(10)
```
### This operation is for the uppercase and lowercase letter password 
```
elif operation == '2':
    def get_random_string(length):
        letters = string.ascii_letters
        result_str = ''.join(random.choice(letters) for i in range(length))
        print("Random letters password is:", result_str)
    get_random_string(10)
```
### This operation is for the alphanumeric password
```
elif operation == '3':
    def get_random_alphanumeric_string(length):
        letters_and_digits = string.ascii_letters + string.digits
        result_str = ''.join(random.choice(letters_and_digits) for i in range(length))
        print("Random alphanumeric password is:", result_str)
    get_random_alphanumeric_string(10)
```
### This is the last operation for the alphanumeric password with special characters
```
    def get_random_password_string(length):
        password_characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(password_characters) for i in range(length))
        print("Random alphanumeric/special characters password is:", password)
    get_random_password_string(10)
```
### If you do not enter a number 1-4 when prompted, the script will ask you to try again
```
else:
    print('You have not entered a valid value, please run the program again')
```
### Sample Output
```
Welcome to the multi-password generator. Please select which type of 10 character password you want:
1 for lowercase letters
2 for uppercase and lowercase letters
3 for letters and numbers
4 for letters, numbers, and special characters
Enter here: 2
Random letters password is: uJx00iaKaw
```
### Reference
I used https://pynative.com/python-generate-random-string/ as a reference for this project
