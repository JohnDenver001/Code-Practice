import random

def is_number_valid(num):
    while True:
        try:
            num_guess = int(input(num))
            return num_guess
        except ValueError:
            print("Please input number only!")

def user_continue():
    while True:
        print("Do you still want to continue?")
        user_cont = "YES or NO: ".upper()
        if user_cont == "YES":
            return True
        elif user_cont == "NO":
            return False
        else:
            print("Please input YES or NO only!")

def user_reset():
    secret_number = random.randint(1, 5)
    print("|  Random Number has been generated  |")
    print("|  The number is in between 1 and 5  |")
    return secret_number

def user_lives(life):
    if life == 3:
        print("You got 3 more guess")
    elif life == 2:
        print("The life's ticking, you only got 2!")
    elif life == 1:
        print("One more guess to go!")
    elif life == 0:
        return False

def main():
    print("===========================")
    print(" Welcome to GUESSING GAME!")
    print("===========================")
    print()

    secret_number = user_reset()

    user_correct = False
    while not user_correct:
        user_guess = is_number_valid("Please input your guess here: ")
        if user_guess == secret_number:
            print(f"{user_guess} is correct!")
            user_correct = True
        else:
            print("Enkk! Wrong Guess!")
            print()

main()