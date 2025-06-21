from helper_function import *
import json

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def show_user_info(self):
        print("===========================")
        print(f"{self.username} CREDENTIALS:")
        print("===========================")
        print(f"USERNAME: {self.username}")
        print(f"PASSWORD: {self.password}")


class System:
    def __init__(self):
        self.accounts = []

    def register_user(self):
        print("Please enter the following information:")
        username = input("Username: ")

        if any(user.username == username for user in self.accounts):
            print("User already exist!")
            return

        password = check_password_len("Enter your password: ")
        hashed = hash_password(password)

        user_credentials = User(username, hashed)
        self.accounts.append(user_credentials)
        print("User Created!")

    def login_user(self):
        print("Login your information:")
        username = input("Username: ")

        for user in self.accounts:
            if user.username == username:
                current_user = user
                break
        else:
            print("User can't found! \n"
                  "Please Register first!")
            return

        password = input("Password: ")
        hashed = hash_password(password)

        if current_user.password == hashed:
            print("Login Successfully!")
        else:
            print("Password do not match!")

    def user_info(self):
        search_name = input("username: ")
        for user in self.accounts:
            if user.username == search_name:
                user.show_user_info()
                return
        else:
            print("User can't be found!")
            return

    def change_password(self):
        search_name = input("Enter your username: ")
        for account in self.accounts:
            if account.username == search_name:
                current_account = account
                break
        else:
            print("User does not exist!\n")
            return

        current_password = input("Enter your current password: ")
        hashed = hash_password(current_password)

        if hashed != current_account.password:
            print("Password incorrect!\n")
            return

        new_password = check_password_len("Enter your new password: ")
        hashed = hash_password(new_password)

        if hashed == current_account.password:
            print("This is your current password\n"
                  "Please try a new one\n")
            return

        current_account.password = hashed
        print("Password successfully changed!")

    def delete_account(self):
        delete_name = input("Enter username you want to delete: ")
        for account in self.accounts:
            if account.username == delete_name:
                self.accounts.remove(account)
                print("Removed account successfully!")
                break
        else:
            print("User does not exist!\n")
            return

    def save_data_to_json(self):
        data = []

        for account in self.accounts:
            account_data = {
                "username": account.username,
                "password": account.password
            }
            data.append(account_data)

        with open("Data.json", "w") as file:
            json.dump(data, file, indent = 4)

    def reload_data_from_json(self):
        try:
            with open("Data.json", "r") as file:
                data = json.load(file)

            for account in data:
                account_credentials = User(username = account["username"], password = account["password"])
                self.accounts.append(account_credentials)

        except FileNotFoundError:
            print("File can't found! -- Starting Fresh")

def main():
    system = System()
    cont = True
    system.reload_data_from_json()

    while cont:
        choice = user_choice()
        if choice == 1:
            system.register_user()
            system.save_data_to_json()
        elif choice == 2:
            system.login_user()
        elif choice == 3:
            system.user_info()
        elif choice == 4:
            system.change_password()
            system.save_data_to_json()
        elif choice == 5:
            system.delete_account()
            system.save_data_to_json()
        elif choice == 6:
            print("Thankyou!")
            return
        cont = user_cont()

main()