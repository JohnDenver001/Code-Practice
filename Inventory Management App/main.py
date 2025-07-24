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
    handle_user_interaction(inventory)

def handle_user_interaction(inventory):
    """Handle user interaction"""

    while True:
        user_action = get_user_action()

        if user_action == 1:
            inventory.add_product()

        elif user_action == 2:
            inventory.remove_product()

        elif user_action == 3:
            inventory.edit_product()

        elif user_action == 4:
            inventory.list_products()

        elif user_action == 5:
            inventory.show_stats()

        elif user_action == 6:
            print("\nThank You!")
            return
        
        if user_action in [1, 2, 3]:
            inventory.save_inventory_to_json()

def main():
    """Main program --- Starts the system"""

    inventory = Inventory()
    user = User(inventory)  
    user.load_user_credentials_from_json() #Load users from user_database path
    user.load_users_inventory() #Load users from inventory_database path

    while True:
        authentication = auth_menu()

        if authentication == 1:
            handle_register(user)
            user.save_user_credentials_to_json() #Save the user's credential to user_database path

        elif authentication == 2:
            handle_login(user, inventory)

if __name__ == "__main__":
    main()
