# PROBLEM
'''Display the following menu to the user: 

1) Addition
2) Subtraction

   
Enter 1 or 2:

If they enter a 1, it should run a subprogram that will 
generate two random numbers between 5 and 20, and 
ask the user to add them together. Work out the correct 
answer and return both the user’s answer and the 
correct answer. 
If they entered 2 as their selection on the menu, it 
should run a subprogram that will generate one number 
between 25 and 50 and another number between 1 and 
25 and ask them to work out num1 minus num2. This 
way they will not have to worry about negative answers. 
Return both the user’s answer and the correct answer. 
Create another subprogram that will check if the user’s 
answer matches the actual answer. If it does, display 
“Correct”, otherwise display a message that will say 
“Incorrect, the answer is” and display the real answer. 
If they do not select a relevant option on the first menu 
you should display a suitable message.'''

# SOLUTION

import random

def add_nums():
    num1 = random.randint(5, 20)
    num2 = random.randint(5, 20)
    user_answer = int(input(f"What is {num1} + {num2}? "))
    correct_answer = num1 + num2
    return (correct_answer, user_answer)


def subtract_nums():
    num1 = random.randint(25, 50)
    num2 = random.randint(1, 25)
    user_answer = int(input(f"What is {num1} - {num2}? "))
    correct_answer = num1 - num2
    return (user_answer, correct_answer)


def check_answer(correct_answer, user_answer):
    if user_answer == correct_answer:
            print("Correct")

    else:
            print(f"Incorrect, the answer is {correct_answer}")


def main():
    print("1) Addition")
    print("2) Subtraction")
    choice = int(input("Enter 1 or 2: "))
    
    if choice == 1:
        user_answer, correct_answer = add_nums()
        check_answer(correct_answer, user_answer)

    elif choice == 2:
        user_answer, correct_answer = subtract_nums()
        check_answer(correct_answer, user_answer)

    else:
        print("Invalid option!")

main()
