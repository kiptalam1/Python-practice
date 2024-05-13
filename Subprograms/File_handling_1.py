'''Create the following menu:

  1) Add to file
  2) View all records
  3) Quit program
  Enter the number of your selection:

If the user selects 1, allow them to add to a file called Salaries.csv which will store their name and salary. If they select 2 it should display all records 
in the Salaries.csv file. If they select 3 it should stop the program. If they select an incorrect option they should see an error message. They should keep 
returning to the menu until they select option 3.'''


import csv

def addtofile():
    file = open("Salaries.csv", "a")
    name = input("Enter name: ")
    salary = int(input("Enter salary: "))
    new_record = name + ", " + str(salary) + "\n"
    file.write(str(new_record))
    file.close()


def view():
    file = open("Salaries.csv", "r")
    for row in file:
        print(row)
    file.close()


try_again = True
while try_again == True:
    print("1) Add to file")
    print("2) View all records")
    print("3) Quit program")
    print()
    selection = int(input("Enter the number of your selection: "))
    if selection == 1:
        addtofile()
    elif selection == 2:
        view()
    elif selection == 3:
        try_again = False
    else:
        print("Invalid option!")
