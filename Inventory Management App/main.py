from classes import *


def handle_register(user):
    """Handle the user registration"""

    user.register()

def handle_login(user, inventory):
    """Handle the user log in and return if not successful"""

    current_user = user.login()

    # Check if the user log in successfully.
    if current_user is None:
        return

    inventory.load_user_inventory_from_json()
    handle_user_interaction(user, inventory)

def handle_user_interaction(current_user, inventory):
    """Handle user interaction"""
    while True:
        user_action = get_user_action()

        if user_action == 1:
            current_user.add_product()
            inventory.save_inventory_to_json()

        elif user_action == 2:
            current_user.remove_product()
            inventory.save_inventory_to_json()

        elif user_action == 3:
            current_user.edit_product()
            inventory.save_inventory_to_json()

        elif user_action == 4:
            inventory.list_products()

        elif user_action == 5:
            inventory.show_stats()

        elif user_action == 6:
            print("\nThank You!")
            return

def main():
    """Main program --- Starts the system"""

    inventory = Inventory()
    user = User(inventory)
    user.load_user_credentials_from_json() #Load users from user_database path
    user.load_users() #Load users from inventory_database path

    while True:
        authentication = auth_menu()

        if authentication == 1:
            handle_register(user)
            user.save_user_credentials_to_json() #Save the user's credential to user_database path

        elif authentication == 2:
            handle_login(user, inventory)

if __name__ == "__main__":
    main()
