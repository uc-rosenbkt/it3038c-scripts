import random
import string
operation = input('''Welcome to the multi-password generator. Please select which type of 10 character password you want:
1 for lowercase letters
2 for lowercase and uppercase letters
3 for letters and numbers
4 for letters, numbers, and special characters
Enter here: ''')

if operation == '1':
    def get_random_string(length):
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(length))
        print("Random lowercase letters password is:", result_str)
    get_random_string(10)

elif operation == '2':
    def get_random_string(length):
        letters = string.ascii_letters
        result_str = ''.join(random.choice(letters) for i in range(length))
        print("Random letters password is:", result_str)
    get_random_string(10)

elif operation == '3':
    def get_random_alphanumeric_string(length):
        letters_and_digits = string.ascii_letters + string.digits3
        result_str = ''.join(random.choice(letters_and_digits) for i in range(length))
        print("Random alphanumeric password is:", result_str)
    get_random_alphanumeric_string(10)

elif operation == '4':
    def get_random_password_string(length):
        password_characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(password_characters) for i in range(length))
        print("Random alphanumeric/special characters password is:", password)
    get_random_password_string(10)

else:
    print('You have not entered a valid value, please run the program again')