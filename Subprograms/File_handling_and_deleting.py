'''In Python, it is not technically possible to directly delete a record from a .csv file. Instead you need to save the file to a temporary list in Python, 
make the changes to the list and then overwrite the original file with the temporary list. Change the previous program to allow you to do this. Your menu 
should now look like this:

  1) Add to file
  2) View all records
  3) Delete a record
  4) Quit program
Enter the number of your selection: this:'''

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


def delete_record():
    file = open("Salaries.csv", "r")
    x = 0
    templist = []
    for row in file:
       templist.append(row)
    file.close()
    for row in templist:
        print(x, row)
        x = x + 1
    rowtodelete = int(input("Enter the record you want to delete: "))
    del templist[rowtodelete]
    
    file = open("Salaries.csv", "w")
    for row in templist:
        file.write(row)
    file.close()

try_again = True
while try_again == True:
    print("1) Add to file")
    print("2) View all records")
    print("3) Delete a record")
    print("4) Quit program")
    print()
    selection = int(input("Enter the number of your selection: "))
    if selection == 1:
        addtofile()
    elif selection == 2:
        view()
    elif selection == 3:
        delete_record()
    elif selection == 4:
        try_again = False
    else:
        print("Incorrect option!")
