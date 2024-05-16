""" Imports random, os and time for hangman """
import random
import os
import time

from words import wordlist
from hangman_picture import stages, logo


def user_name_input():
    """
    Function that asks user for their name and greets them to the game,
    additionally limits the length of the name to 25 characters.
    """
    name = input("\nPlease enter your name: \n").strip()
    while len(name) > 25:
        print("\nYour name is too long for this program.")
        print("Please make it shorter.\n")
        time.sleep(1)
        clear()
        name = input("\nPlease enter your name: \n").strip()
    while len(name) == 0:
        print("You must enter a name.")
        time.sleep(1)
        clear()
        name = input("\nPlease enter your name: \n").strip()

    print("-" * 25)
    print(f"\nHello {name} and welcome to Hangman Game\n")
    time.sleep(3)
    clear()
    return name


def get_menu():
    """
    Displays the menu and returns the user options.
    """
    clear()
    print(logo)
    print("Welcome to the Hangman Game!!!")
    print("Main Menu:")
    print("1.Start New Game")
    print("2.How To Play")
    print("3.Exit")
    while True:
        choice = input("Enter your choice (1/2/3): ").strip()
        try:
            choice = int(choice)
            if choice > 3 or choice < 1:
                print("Invalid input! Enter your choice (1/2/3):").strip()
                continue
        except ValueError:
            print("Invalid input! Enter your choice (1/2/3):").strip()
            continue
        return choice


def how_to_play():
    """
    Displays the game instructions & how to play.
    """
    clear()
    print(logo)
    print("\nHangman is a word-guessing game where you have to guess a "
          "hidden word letter by letter.\n")
    print("If you guess correctly the letters will be shown in their "
          "appropriate place.\n")
    print("You can make a limited number of incorrect guesses before the "
          "hangman is complete.\n")
    print("Your goal is to guess the word before the hangman"
          "is fully drawn.\n")
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


def main(name=''):
    """
    Main function for executing the Hangman game.
    if player's name not provided, it will prompt the user for input.
    """
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
        how_to_play()
        main()
    else:
        if name == '':
            name = user_name_input()  # Call method to get user's name
        display = ["_" for _ in range(word_length)]
        current_guesses = []
        current_message = ''
        while not end_of_game:
            guess = display_part(lives, display, current_message)

            if guess in current_guesses:
                current_message = f"You've already guessed {guess}"
            elif guess not in chosen_word:
                lives -= 1
                current_message = (f"You guessed: {guess}, it's not in the "
                                   "word. You lose a life.")
                if lives == 0:
                    end_of_game = True
                    clear()
                    print(stages[lives])
                    print("You are out of lives!")
                    print(f"The word was: {chosen_word}.")
                    print("You lost the Game. Better luck next time!")
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
                print(f"{name}, You got it!")
                print(f"The word was: {chosen_word}.")
                print("You won !! Great job!")

        while True:
            play_again = input("play again? Y or N: ").lower().strip()
            if play_again not in ["y", "n"]:
                print("Invalid input!")
            elif play_again == 'y':
                main(name)
            else:
                print("Thank you for playing Hangman. Have a Good day!")
                exit()


main()

