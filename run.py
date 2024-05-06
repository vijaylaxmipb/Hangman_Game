import string
import random
import os
import time

from words import wordlist
from hangman_picture import stages

def user_name_input():
    """
    Function that asks user for their name and greets them to the game,
    additionally limits the lenght of the name to 23 characters.
    Info: Any character is allowed in case one wants to use their
    username instead of real name - or X Æ A-12 Musk (Son of Elon Musk)
    would like to play.
    """
    name = input("\nPlease enter your name: \n")
    while len(name) <= 23:
        if len(name) > 0:
            break
        else:
            print("You must enter a name.")
            time.sleep(1)
            clear()
            return user_name_input()
    else:
        print("\nYour name is too long for this program.")
        print("Please make it shorter.\n")
        time.sleep(1)
        clear()
        return user_name_input()

    print("-" * 23)
    print(f"\nHello {name} and welcome to Hangman Game\n")
    time.sleep(3)
    clear()
    return name


def get_menu():
    """
    Displays the memu and returns the user options.
    """
    clear()
    print("Welcome to the Hangman Game!!!")
    print("Main Menu:")
    print("1.Start New Game")
    print("2.How To Play")
    print("3.Exit")
    while True:
        choice = input("Enter your choice (1/2/3): ")
        try:
            choice = int(choice) 
            if choice > 3 or choice < 1:
                print("Invalid input! Enter your choice (1/2/3): ")
                continue
        except ValueError:
                print("Invalid input! Enter your choice (1/2/3):")
                continue
        return choice
            
def  How_to_play():
    """
    Displays the game instructions & how to play.
    """
    clear()
    print("\nHangman is a word-guessing game where you have"
          " to guess a hidden word letter by letter.")
    print("You can make a limited number of incorrect guesses"
          " before the hangman is complete.")
    print("Your goal is to guess the word before the hangman is fully drawn.")
    print("Good luck!\n")
    input("Press ENTER to continue")
    
def clear():
    """
    Clears the terminal 
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def display_part(lives, guesses, message):
    """
    Displays the current part of the Hangman Game.
    """
    clear()
    print(stages[lives])
    print(f"{' '.join(guesses)}")
    print(message)
    while True:
        guess = input("Guess a letter:").lower()
        if len(guess) == 0:
            print("Guess cannot be empty")
        elif len(guess) > 1:
            print("Guessed letter should not be more than one character")
        elif not guess.isalpha():
            print("Guess should be a letter")
        else:
            print(f"You guessed: {guess}")  # Print the guessed letter
            return guess

def main():
    name = user_name_input()  # Call user_name_input() to get the user's name
    chosen_word = random.choice(wordlist)
    word_length = len(chosen_word)

    end_of_game = False
    lives = 6

    menu_choice = get_menu()
    if menu_choice == 3:
        end_of_game = True
        print("Goodbye!")
        return
    elif menu_choice == 2:
        How_to_play()
        main()
    else:
        display = ["_" for _ in range(word_length)]
        current_guesses = []
        current_message = ''
        while not end_of_game:
            guess = display_part(lives, display, current_message)

            if guess in current_guesses:
                current_message = f"You've already guessed {guess}"
            elif guess not in chosen_word:
                lives -= 1
                current_message = f"You guessed {guess}"
                "that's not in the word.You lose a life."
                if lives == 0:
                    end_of_game = True
                    clear()
                    print(stages[lives])
                    print("You are out of lives!")
                    print(f"The word was: {chosen_word}.")
                    print("You lose. Good luck next time!")
            else:
                for position in range(word_length):
                    letter = chosen_word[position]
                    if letter == guess:
                        current_message = "Correct guess!"
                        display[position] = letter
            current_guesses.append(guess)
            if "_" not in display:
                end_of_game = True
                clear()
                print(stages[lives])
                print("You got it!")
                print(f"The word was: {chosen_word}.")
                print("You win! Great job!")

        while True:
            play_again = input("Do you want to play again? Y or N: ").lower()
            if play_again not in ["y", "n"]:
                print("Invalid input!")
            elif play_again == 'y':
                main()
            else:
                print("Thank you for playing Hangman. Goodbye!")
                return
main()



