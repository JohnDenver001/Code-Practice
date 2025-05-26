import random
def validate_number(word):
    while True:
        try:
            number = int(input(word))
            return number
        except ValueError:
            print("Please enter number only!")
            print()

def difficulty():
    while True:
        difficulty_level = validate_number("Please choose difficulty level: \n"
                                           "[1] Easy \n"
                                           "[2] Medium \n"
                                           "[3] Hard \n"
                                           "Choice (1-3): ")
        if difficulty_level == 1:
            first = 1
            second = 10
        elif difficulty_level == 2:
            first = 1
            second = 30
        elif difficulty_level == 3:
            first = 1
            second = 50
        else:
            print("Please enter number 1-3 only! ")
            print()
            continue
        return first, second

def user_continue():
    while True:
        cont = input("Do you still want to continue? (YES or NO): ").upper()
        if cont == "YES":
            print()
            return True
        elif cont == "NO":
            print("Thank you!")
            return False
        else:
            print("Please enter YES or NO only!")

def clue(guesses, secret):
    if guesses > secret:
        print("Too High!")
    elif secret > guesses:
        print("Too Low!")

def best_tries(life, best_trys):
    if life > best_trys:
        best_trys = life
        print(f"Congrats on your new high score: {best_trys}\n")
    else:
        print(f"Current score: {life}\n"
              f"High score: {best_trys}\n")
    return best_trys

def main_game(secret_number):
    life = 5
    while life > 0:
        print(f"You have {life} remaining tries")
        guess = validate_number("Enter your guess: ")
        if secret_number == guess:
            print("Correct!")
            print()
            break
        else:
            clue(guess, secret_number)
            life -= 1
            print("Incorrect")
            print()
    if life == 0:
        print("You died! \n"
              "Better luck next time!")
        print()
    return life

def main():
    player_name = input("Name: ")
    print(f"Goodluck, {player_name}!")
    print()

    best_try = 0
    user_cont = True
    while user_cont:
        a, b = difficulty()
        secret_number = random.randint(a, b)
        print("Number has been generated.")
        print()
        best_try = best_tries(main_game(secret_number), best_try)

        user_cont = user_continue()

main()

