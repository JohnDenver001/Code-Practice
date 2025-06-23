from classes import *

def handle_register(system):
    system.register()
    system.save_data_json()

#This comes after user chooses login
def handle_user_action(system):
    username, log_in_success = system.login()

    if log_in_success is False:
        return True

    while log_in_success:
        action_choice = user_action_choice(username)

        if action_choice == 1:
            handle_income(system)

        elif action_choice == 2:
            handle_expense(system)

        elif action_choice == 3:
            system.user_logout()
            return False

def handle_income(system):
    income_type = add_income()

    if income_type == 1:
        system.add_main_income()
        system.save_data_json()

    elif income_type:
        system.add_side_income()
        system.save_data_json()

def handle_expense(system):
    expense_type = add_expense()

    if expense_type == 1:
        system.add_type_expense("food_expense")
        system.save_data_json()

    elif expense_type == 2:
        system.add_type_expense("rent_expense")
        system.save_data_json()

    elif expense_type == 3:
        system.add_type_expense("clothing_expense")
        system.save_data_json()

    elif expense_type == 4:
        system.add_type_expense("other_expense")
        system.save_data_json()

def main():
    system = System()
    system.reload_data_from_json()
    user_cont = True

    while user_cont:
        welcome_user_choice = welcome_user()

        if welcome_user_choice == 1:
            handle_register(system)

        elif welcome_user_choice == 2:
            user_cont = handle_user_action(system)

main()