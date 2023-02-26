# Author:Zuriahn Yun
# Date: 2/21/2023
# Description:Lottery Game Lab 7 

import sys
import random

def random_pick(words, numbers):
    """ Generate a random winning lottery pick. The winning
    pick is a string containing one item from words (a list
    of strings) and one item from numbers (a list of ints),
    concatenated in a randomly chosen order. The random
    choices are made independently, so the chance of each
    possible pick is equal."""
    
    # (TASK 1) - Pseudocode:
    # Pick one of the numbers randomly
    # Pick one of the words randomly  
    # Pick which order they go in randomly
    # return the combined lottery pick as a string
    
    
    #Picking a random number and word
    word = random.choice(words)
    number = random.choice(numbers)
    #Converting the number to a string
    number = str(number)
    #Randomly picking the order and returning the number and word as one
    order = random.randint(1,2)
    if order == 2:
        list=(number,word)
        win = ''.join(list)
        return win
    else:
        list = (word,number)
        win = ''.join(list)
        return win

def get_guess(words, numbers):
    """ Prompt the user until they enter a pick that contains one
        of the given words and begins or ends with one
        of the given numbers. When a valid guess is entered, return
        it.
        Precondition: numbers contains only one-digit numbers. """
    
    # (TASK 2) - Pseudocode:
    # while the user has not entered a valid pick:
    #    prompt the user for a pick
    #    check if it's valid (see docstring for the precise definition of valid)
    #    if not, print a message saying what's missing
    #    if it is, return the valid pick
    #Asking the user for a lottery pick
    number_list = (numbers)
    word_list = (words)
    lottery = input("Enter your pick:")
    return lottery

def main():
    """ Generate a lottery pick and check whether a user has guessed it
        correctly.  """
    word_choices = ["shucksan", "baker", "glacier"]
    number_choices = ["1", "2", "3"]
    
    print("Welcome, and thanks for playing Lotter.io!")
    print("Today's word choices are:", end=" ")
    print(word_choices)
    print("and the number choices are", end=" ")
    print(number_choices)
    print("The winning pick is a word and a number, in either order.")

    # (TASK 0) - Pseudocode:
    # if the program was run with no command line arguments:
    #     generate a winning pick by calling the random_pick function
    # otherwise:
    #     use the first command-line argument as the winning pick
    
    #If no argument is given randomly pick one
    if len(sys.argv) > 1:
        winning_pick = sys.argv[1]
    else:
        winning_pick = random_pick(word_choices,number_choices)
    valid_number = 0
    valid_word = 0
            
    # Get a guess from the user:
    
    #While loop if guess is not valid
    while valid_number == 0 and valid_word == 0:
        guess = get_guess(word_choices,number_choices)
   
    
    #check if the guess is valid. If it is not, ask again.
        

            
    # (TASK 3) - Pseudocode:
    # determine the user's word and number choices by checking
    # whether the first or last character is among number_choices,
    # then split the string into the number part and the word part
    
    #Finding the number and using it to see if the guess is valid and to find the word
        last = guess[-1]
        first = guess[0]
        if last in number_choices:
            guess_number = last
            guess_word = (guess[0:-2])
            valid_number = 1
            valid_word = 1
        elif first in number_choices:
            guess_number = first
            guess_word = (guess[1:-1])
            valid_number = 1
            valid_word = 1
        else:
                guess = get_guess(word_choices,number_choices)
    
    # print a message for whichever of the following cases is applicable:
    #   - their pick matches character for character, therefore they win
    #   - the word and number are both correct but the pick doesn't match
    #   - the word is correct but the number is incorrect
    #   - the number is correct but the word is incorrect
    #   - all other cases: neither the word nor the number is correct
    
    #If elif else statment depending on user response to dictate what you get for the lottery pick
    if guess == winning_pick:
        print("Your guess is correct, you win oranges!")
    elif guess_number in winning_pick and guess_word in winning_pick:
        print("Your word and number are correct but your pick doesnt match")
    elif guess_number in winning_pick and guess_word not in winning_pick:
        print("Your number is correct but your word is incorrect")
    elif guess_word in winning_pick and guess_number not in winning_pick:
        print("Your word is correct but your number is incorrect")
    else:
        print("Your word and number were incorrect")     
if __name__ == "__main__":
    main()