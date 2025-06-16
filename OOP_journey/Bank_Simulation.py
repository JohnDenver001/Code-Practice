from Bank_Simulation_Function import *
import random
user_list = []
bank_accounts_list = []

class User:
    def __init__(self, name, id, age, status, sex):
        self.name = name
        self.id = id
        self.age = age
        self.status = status
        self.sex = sex

    def show_user_info(self):
        print("====================================")
        print(f"{self.name}'s INFORMATION")
        print(f"Name: {self.name}")
        print(f"ID number: {self.id}")
        print(f"Age: {self.age}")
        print(f"Status: {self.status}")
        print(f"Sex: {self.sex}")
        print("====================================")

class BankAccount(User):
    def __init__(self, name, id, age, status, sex, bank_id, bank_cash_amount, bank_expiration_date):
        super().__init__(name, id, age, status, sex)
        self.bank_id = bank_id
        self.cash_amount = bank_cash_amount
        self.expiration_date = bank_expiration_date

    def showBankAccountStatus(self):
        print("===================================")
        print(f"{self.name}'s Bank Account Status")
        print(f"Bank ID: {self.bank_id}")
        print(f"Cash Amount: {self.cash_amount}")
        print(f"Bank Expiration Date: {self.expiration_date}")
        print("===================================")

def user_choice():
    print("=========================================")
    print("        WELCOME TO BANK SIMULATION")
    print("=========================================")
    print("[1] Register User")
    print("[2] Register User Bank Account")
    print("[3] Show User Info")
    print("[4] Show User Bank Status")
    print("[5] Deposit")
    print("[6] Withdraw")
    print("[7] Transfer")
    print("[8] Exit")
    print("=========================================")
    while True:
        choice = validate_integer("What would you like to do (1-9): ")

        if choice < 1 or choice > 8:
            print("Enter 1-9 only!\n")
        else:
            return choice

def register_user():
    print("Enter the following User Information:")
    user_name = input("Name: ").title()
    user_id = validate_integer("ID number: ")
    user_age = validate_integer("Age: ")
    user_status = input("Status: ")
    user_sex = input("Sex: ")

    for user in user_list:
        if user.id == user_id:
            print("User already exist!")
            return
    user = User(user_name, user_id, user_age, user_status, user_sex)

    user_list.append(user)
    print(f"User Created! Welcome {user_name}!")

def register_user_into_bank():
    random_number = random.randint(100, 103)
    user_bank_id = validate_integer("Please input your ID number here: ")

    for bank_account in bank_accounts_list:
        if bank_account.bank_id == random_number:
            random_number = random.randint(100, 103)

        if bank_account.id == user_bank_id:
            print("User already registered in Bank!")
            return

    for user in user_list:
        if user.id == user_bank_id:
            user_bank = BankAccount(user.name, user.id, user.age, user.status, user.sex, random_number, 0, 2005)
            bank_accounts_list.append(user_bank)
            print("User registered successfully!")
            print(f"Your Bank ID is: {random_number}")
            return
    print("User can't be found!")
    return

def show_user():
    search_id = validate_integer("Enter ID: ")

    for user in user_list:
        if user.id == search_id:
            user.show_user_info()
            return
    print("User can't be found!")

def show_user_bank_status():
    search_id = validate_integer("Enter ID: ")
    for bank_account in bank_accounts_list:
        if bank_account.bank_id == search_id:
            bank_account.showBankAccountStatus()
            return
    print("User can't be found!")

def deposit():
    deposit_id = validate_integer("Enter your Bank ID: ")
    deposit_amount = validate_integer("Enter the amount you want to deposit: ")

    for account in bank_accounts_list:
        if account.bank_id == deposit_id:
            account.cash_amount += deposit_amount
            print(f"{deposit_amount} has been deposited into your account! \n")
            account.showBankAccountStatus()
            return

    print("User can't be found!")
    return

def withdraw():
    withdraw_id = validate_integer("Enter your Bank ID: ")
    withdraw_amount = validate_integer("Enter the amount you want to deposit: ")

    for account in bank_accounts_list:
        if account.bank_id != withdraw_id:
            continue

        if account.cash_amount < withdraw_amount:
            print("You don't have enough balance in your account!\n"
                  "Please deposit first! ")
            return

        account.cash_amount -= withdraw_amount
        print(f"{withdraw_amount} has been withdrawn from your bank account! \n")
        account.showBankAccountStatus()
        return

    print("User can't be found!")
    return

def transfer():
    transfer_id = validate_integer("Enter your Bank ID: ")
    receiver_id = validate_integer("Enter the Bank ID where you want to transfer your money: ")
    transfer_amount = validate_integer("Enter how much you want to transfer: ")

    transfer_account = None
    receiver_account = None

    for account in bank_accounts_list:
        if account.bank_id == transfer_id:
            transfer_account = account
        if account.bank_id == receiver_id:
            receiver_account = account

    if not transfer_account:
        print(f"Your Bank ID: {transfer_id} is not registered in bank!")
        return

    if not receiver_account:
        print(f"Receiver Bank ID: {receiver_id} is not registered in bank!")
        return

    if transfer_account == receiver_account:
        print("You can't transfer to your own account!")
        return

    if transfer_account.cash_amount < transfer_amount:
        print("You don't have enough balance in your account!\n"
              "Please deposit first! ")
        return

    transfer_account.cash_amount -= transfer_amount
    receiver_account.cash_amount += transfer_amount

    print(f"{transfer_amount} has been transfered to {receiver_account.name}")
    print("Both account has now been updated")
    transfer_account.showBankAccountStatus()
    receiver_account.showBankAccountStatus()
    return




def main():
    user_continues = True
    while user_continues:
        choice = user_choice()
        if choice == 1:
            register_user()
        elif choice == 2:
            register_user_into_bank()
        elif choice == 3:
            show_user()
        elif choice == 4:
            show_user_bank_status()
        elif choice == 5:
            deposit()
        elif choice == 6:
            withdraw()
        elif choice == 7:
            transfer()
        elif choice == 8:
            print("Thankyou!")
            return
        user_continues = user_cont()

main()
#Ended in line 83 to check if user exist
#Fail to check user does exist