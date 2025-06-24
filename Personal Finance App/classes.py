import json
from helper_function import *
from datetime import datetime

class User:
    def __init__(self, username, password, main_income, side_income, food_expense, rent_expense, clothing_expense, other_expense):
        self.username = username
        self.password = password
        self.main_income = main_income
        self.side_income = side_income
        self.food_expense = food_expense
        self.rent_expense = rent_expense
        self.clothing_expense = clothing_expense
        self.other_expense = other_expense

class System:
    def __init__(self):
        self.accounts = []
        self.current_user = None

    def save_data_json(self):
        data = []
        for account in self.accounts:
            account_data = {
                "username": account.username,
                "password": account.password,
                "income": {
                    "main_income": account.main_income,
                    "side_income": account.side_income
                },
                "expense": {
                    "food_expense": date_strf_expense(account, "food_expense"),
                    "rent_expense": date_strf_expense(account, "rent_expense"),
                    "clothing_expense": date_strf_expense(account, "clothing_expense"),
                    "other_expense": date_strf_expense(account, "other_expense")
                }
            }
            data.append(account_data)

        with open("Finance_App_Data.json", "w") as file:
            json.dump(data, file, indent = 4)

    def reload_data_from_json(self):
        try:
            with open("Finance_App_Data.json", "r") as file:
                data = json.load(file)

            for account in data:
                account_credentials = User(username = account["username"],
                                           password = account["password"],
                                           main_income = account["income"]["main_income"],
                                           side_income = account["income"]["side_income"],
                                           food_expense = date_strp_expense(account["expense"]["food_expense"]),
                                           rent_expense = date_strp_expense(account["expense"]["rent_expense"]),
                                           clothing_expense = date_strp_expense(account["expense"]["clothing_expense"]),
                                           other_expense = date_strp_expense(account["expense"]["other_expense"])
                                           )

                self.accounts.append(account_credentials)

        except FileNotFoundError:
            print("File not found! -- Starting Fresh!\n")

    def register(self):
        print("========================")
        print("        REGISTER")
        username = input("Enter username: ")
        password = input("Enter password: ")

        for account in self.accounts:
            if username == account.username:
                print("Account is already registered!\n")
                return

        if len(password) < 8:
            print("Password too weak!\n")
            return

        hashed_password = hash_password(password)
        account_credentials = User(username, hashed_password, 0, 0, [], [], [], [])
        self.accounts.append(account_credentials)
        print("Account created successfully!\n"
              f"Welcome {username}")
        return username

    def login(self):
        print("========================")
        print("        LOGIN")
        username = input("Enter username: ")
        password = input("Enter password: ")
        hashed_password = hash_password(password)

        for account in self.accounts:
            if username == account.username:
                current_account = account
                break
        else:
            print("Account is not registered!\n"
                  "Please register first!\n")
            return None, False

        if current_account.password != hashed_password:
            print("Password don't match!\n")
            return None, False

        print("Account login successfully!\n")
        self.current_user = current_account
        return username, True

    def add_main_income(self):
        main_income_amount = validate_integer("Enter your main income amount: ")
        self.current_user.main_income = main_income_amount
        print("Your main income has been updated successfully!\n")

    def add_side_income(self):
        side_income_amount = validate_integer("Enter your side income amount: ")
        self.current_user.side_income = side_income_amount
        print("Your side income has been updated successfully!\n")

    def add_type_expense(self, type_name):
        expense_info = get_expense_info()
        getattr(self.current_user, type_name).append(expense_info)
        print(f"Your {type_name.replace('_',' ')} has been updated!")

    def user_logout(self):
        while True:
            log_out = input("Confirm logout (YES or NO): ").upper()

            if log_out == "YES":
                self.current_user = None
                return
            elif log_out == "NO":
                return
            else:
                print("Enter 'YES' or 'NO' only!\n")

    def show_user_dashboard(self):
        total_income = self.current_user.main_income + (self.current_user.side_income * 4)

        total_food_expense = sum(expense["expense_amount"] for expense in self.current_user.food_expense)
        total_rent_expense = sum(expense["expense_amount"] for expense in self.current_user.rent_expense)
        total_clothing_expense = sum(expense["expense_amount"] for expense in self.current_user.clothing_expense)
        total_other_expense = sum(expense["expense_amount"] for expense in self.current_user.other_expense)

        total_expense = total_food_expense + total_rent_expense + total_clothing_expense + total_other_expense

        print("===================================")
        print(f"    {self.current_user.username} DASHBOARD")
        print(f"Total Monthly Income: {total_income}")
        print(f"Total Expense: {total_expense}")
        print("===================================\n")

    def reco_budget_plan(self):
        total_income = self.current_user.main_income + (self.current_user.side_income * 4)

        needs_allocation = total_income * .50
        savings_allocation = total_income * .20
        wants_allocation = total_income * .30

        print("=====50-30-20 RULE BUDGET=====")
        print(f"Needs Allocation: {needs_allocation}")
        print(f"Savings Allocation: {savings_allocation}")
        print(f"Wants Allocation: {wants_allocation}")
        print("==============================\n"
              "This is solely based on your income\n"
              "You can adjust this anytime you want.\n")
