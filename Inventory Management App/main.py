from classes import *


def main():
    inventory = Inventory()
    inventory.load_data_from_json()

    while True:
        user_action = get_user_action()
        if user_action == 1:
            inventory.add_product()
            inventory.save_data_to_json()

        elif user_action == 2:
            inventory.remove_product()
            inventory.save_data_to_json()

        elif user_action == 3:
            inventory.edit_product()
            inventory.save_data_to_json()

        elif user_action == 4:
            inventory.list_products()

        elif user_action == 5:
            inventory.show_stats()

        elif user_action == 6:
            print("\nThank You!")
            return

main()
