# PROBLEM

''' Define a subprogram that will ask the user to pick a low and a high number, and then generate a random number between those two values and store it in 
a variable called “comp_num”. Define another subprogram that will give the instruction “I am thinking of a number…” and then ask the user to guess the number they 
are thinking of. Define a third subprogram that will check to see if the comp_num is the same as the user’s guess. If it is, it should display the message “Correct, you 
win”, otherwise it shouldkeep looping, telling the user if they are too low or too high and asking them to guess again until they guess correctly.'''

# SOLUTION

import random
def pick_num():
    low_num = int(input("Enter a low number: "))
    high_num = int(input("Enter a high number: "))
    comp_num = random.randint(low_num, high_num)
    return comp_num

def guess_num():
    print("I am thinking of a number...")
    guess = int(input("Guess the number: "))
    return guess

def check(comp_num, guess):
    try_again = True
    while try_again == True:
        if comp_num == guess:
            print("Correct, you win")
            try_again = False
            
        elif guess < comp_num:
            guess = int(input("Too low! try again: "))
        
        else:
            guess = int(input("Guess the number: "))
        
def main():
    comp_num = pick_num()
    guess = guess_num()
    check(comp_num, guess)

main()
