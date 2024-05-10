'''Create a program that will allow the user to easily manage a list of names. You should 
display a menu that will allow them to add a name to the list, change a name in the 
list, delete a name from the list or view all the names in the list. There should also be a 
menu option to allow the user to end the program. If they select an option that is not 
relevant, then it should display a suitable message. After they have made a selection 
to either add a name, change a name, delete a name or view all the names, they 
should see the menu again without having to restart the program. The program 
should be made as easy to use as possible. '''

def add_name():
    name = input("Enter the name: ")
    names.append(name)
    return names

def change_name():
    num = 0
    for x in names:
        print(num, x)
        num = num + 1
        select_num = int(input("Select the name that you want to change: "))
        name = input("Enter a new name: ")
        names[select_num] = name
        return names

def delete_name():
    num = 0
    for x in names:
        print(num, x)
        select_num = int(input("Which name do you want to delete? "))
        del names[select_num]
        return names

def view():
    for x in names:
        print(x)
    print()


def main():
    again = "y"
    while again == "y":
        print("1) Add name")
        print("2) Change name")
        print("3) Delete name")
        print("4) View")
        print("5) Exit")
        selection = int(input("What do you want to do? "))
        if selection == 1:
            names = add_name()
        elif selection == 2:
            names = change_name()
        elif selection == 3:
            names = delete_name()
        elif selection == 4:
            names = view()
        elif selection == 5:
            again = "n"
        else:
            print("Incorrect option! ")
        data = (names, again)
            

names = []
main() 
