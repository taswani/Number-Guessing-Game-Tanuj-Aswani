import random

global high_score

def start_game():
    # write your code inside this function.
    print("Welcome to the Number Guessing Game! \n")
    random_number = random.randint(1, 10)
    num_guesses = 1
    high_score = 0
    game_done = False
    while not game_done:
        print("Try to guess a number between 1 and 10")
        while True:
            try:
                guess = int(input("What do you think the number is?  "))
                if guess > 10:
                    print("Please enter a number between 1 and 10 \n")
                elif guess < 1:
                    print("Please enter a number between 1 and 10 \n")
                else:
                    break
            except ValueError:
                print("That isn't a number! Please try again... \n")
        if guess > random_number:
            print("\n\033[1m The number is lower than your guess! \033[0m\n")
            num_guesses += 1
            continue
        elif guess < random_number:
            print("\n\033[1m The number is higher than your guess! \033[0m\n")
            num_guesses += 1
            continue
        elif guess == random_number:
            print("\n\033[1mCongrats! You guessed the number! \033[0m\n")
            print("It took", num_guesses, "tries for you to guess the number!\n")
            if num_guesses < high_score or high_score == 0:
                high_score = num_guesses
            print("Current high score is {}!\n".format(high_score))
            while True:
                restart = input("The game is now over. Would you like to play again? Y/N  \n")
                if restart.lower() == "y":
                    num_guesses = 1
                    break
                elif restart.lower() == "n":
                    print("Goodbye!")
                    game_done = True
                    break
                else:
                    print("\n\033[1mPlease enter either Y or N.\033[0m\n")
                    continue
            continue


if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()
