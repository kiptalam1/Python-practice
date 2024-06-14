#Parent Class
class User:
    def __init__(self, name: str, age: int, gender: str):
        self.name = name
        self.age = age
        self.gender = gender

    def show_details(self):
        #display user details.
        print("\nName: ", self.name)
        print("Age: ", self.age)
        print("Gender: ", self.gender)

        
#Child Class        
class Bank(User):
    def __init__(self, name: str, age: int, gender: str):
        super().__init__(name, age, gender)
        self.balance = 0

    def deposit(self, amount: float):
        if amount == 0:
            print("Deposit amount must be more than Ksh 0.")
            return
        elif amount < 0:
            print("Deposit amount must be positive.")
            return
        else:
            self.balance += amount
        print(f"Account has been updated successfully.\nBalance: Ksh {self.balance:.2f}")
        
    def withdraw(self, amount: float):
        if amount == 0:
            print("Withdraw amount must be more than Ksh 0.")
            return
        elif amount < 0:
            print("Withdrawal amount must be positive.")
            return
        
        elif amount > self.balance:
            print(f"Insufficient Funds! Available balance is: Ksh {self.balance:.2f}")
        else:
            self.balance -= amount
            print(f"Ksh {amount:.2f} has been withdrawn successfully.\nAccount balance is: Ksh {self.balance:.2f}")

    def view_balance(self):
        self.show_details()
        print(f"\nAccount Balance: Ksh {self.balance:.2f}")
