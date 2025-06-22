from classes import *

def handle_register(system):
    system.register()
    system.save_data_json()

    handle_user_action(system)

#This comes after user chooses login
def handle_user_action(system):
    username, log_on_account, log_on = system.login()

    while log_on:
        action_choice = user_action_choice(username)

        if action_choice == 1:
            handle_income(system, log_on_account)
        elif action_choice == 2:
            handle_expense(system, log_on_account)
        elif action_choice == 3:
            log_on = user_logout()

def handle_income(system, log_on_account):
    income_type = add_income()

    if income_type == 1:
        add_main_income(log_on_account)
        system.save_data_json()

    elif income_type:
        system.add_side_income(log_on_account)
        system.save_data_json()

def handle_expense(system, log_on_account):
    expense_type = add_expense()

    if expense_type == 1:
        add_food_expense(log_on_account)
        system.save_data_json()

    elif expense_type == 2:
        add_rent_expense(log_on_account)
        system.save_data_json()

    elif expense_type == 3:
        add_clothing_expense(log_on_account)
        system.save_data_json()

    elif expense_type == 4:
        add_other_expense(log_on_account)
        system.save_data_json()

def main():
    system = System()
    system.reload_data_from_json()

    welcome_user_choice = welcome_user()

    if welcome_user_choice == 1:
        handle_register(system)

    elif welcome_user_choice == 2:
        handle_user_action(system)

main()