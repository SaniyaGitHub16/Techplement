import random
import string

def generate_password(length_pass, complexity_pass):
    if complexity_pass == 1:
        characters = string.ascii_letters + string.digits
    elif complexity_pass == 2:
        characters = string.ascii_letters + string.digits + string.punctuation
    elif complexity_pass == 3:
        characters = string.ascii_letters + string.digits + string.punctuation + string.ascii_uppercase + string.ascii_lowercase
    else:
        print("Invalid complexity level. Please choose from '1',' '2' , or '3'.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length_pass))
    return password

def main():
    print("Welcome to the Random Password Generator!")
    while True:
        try:
            length_pass = int(input("Enter the length of the password: "))
            complexity_pass = int(input("Enter the complexity level (1 for low/2 for medium/3 for high): "))
            password = generate_password(length_pass, complexity_pass)
            if password:
                print("Your Generated Password:", password)
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer for password length.")

if __name__== "__main__":
    main()
