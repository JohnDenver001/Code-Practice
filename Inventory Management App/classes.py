from helper_function import *
import json
import os

inventory_database_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "Inventory_Database.json"
)
user_database_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "User_Database.json"
)

class Products:
    """Hold the product informations"""

    def __init__(
        self,
        product_name,
        product_id,
        product_quantity,
        product_price,
        product_category,
    ):
        self.product_name = product_name
        self.product_id = product_id
        self.product_quantity = product_quantity
        self.product_price = product_price
        self.product_category = product_category

class Inventory:
    def __init__(self):
        self.user_inventory_list = [] #List of all users' inventory who have registered
        self.current_user = None #Hold the current user who have logged on
        self.current_user_inventory = [] #Hold the current user inventory -- In Product() object form
        self.product_category_list = [
            "groceries",
            "clothing",
            "electronics",
            "tools",
            "toys",
        ]  # List of available product category

    def save_inventory_to_json(self):
        """Save the product data's added by user"""

        #Convert user current inventory from Product() to dict
        temp_current_user_inventory = [] #Temporarily hold the current user inventory  -- In dict form

        for product in self.current_user_inventory:
            product_information = {
                "product_name": product.product_name,
                "product_id": product.product_id,
                "product_quantity": product.product_quantity,
                "product_price": product.product_price,
                "product_category": product.product_category
            }
            temp_current_user_inventory.append(product_information)

        #Load the 'Inventory_Database' file
        with open(inventory_database_path, "r") as file:
            data = json.load(file)

        all_user_list = [] #Temporarily stores all the users inventory -- In dict form

        for user in data: #Loop through each users in data
            if user["username"] != self.current_user["username"]:
                all_user_list.append(user)
                continue
            else:
                user["inventory"] = temp_current_user_inventory
                all_user_list.append(user)
        
        with open(inventory_database_path, "w") as file:
            json.dump(all_user_list, file, indent = 4)

    def load_user_inventory_from_json(self):
        """Convert user current inventory from dictionaries to Product()"""

        for user_product in self.current_user["inventory" ]:
            product_information = Products(
                product_name = user_product["product_name"],
                product_id = user_product["product_id"],
                product_quantity = user_product["product_quantity"],
                product_price = user_product["product_price"],
                product_category = user_product["product_category"],
            )
            self.current_user_inventory.append(product_information)
        
    def list_products(self):
        print(f"=" * 60)
        print(f"{'PRODUCT LIST':^60}")
        print(f"=" * 60)
        print(f"{'No.':<5} {'ID':<8} {'Name':<15} {'Qty':<10} {'Price':<10} {'Category':<9}")
        print(f"=" * 60)
        
        for i, product in enumerate(self.current_user_inventory):
            print(f"{f'[{i + 1}]':<5} {product.product_id:<8} {product.product_name:<15} {product.product_quantity:<10} {product.product_price:<10} {product.product_category:<8}")

    def show_stats(self):
        """Shows the current status of user's inventory and shows the breakdown of products category"""
        total_products = len(self.current_user_inventory)
        total_quantity = 0
        total_value = 0

        category_counts = {
            "groceries": 0,
            "clothing": 0,
            "electronics": 0,
            "tools": 0,
            "toys": 0,
        }

        for product in self.current_user_inventory:
            total_quantity += product.product_quantity
            total_value += product.product_quantity * product.product_price

            if product.product_category in category_counts:
                category_counts[product.product_category] += 1

        print("========INVENTORY STATUS========")
        print(f"Total Products: {total_products}")
        print(f"Total Quantity: {total_quantity}")
        print(f"Total Value: {total_value}\n")
        print("=======CATEGORY BREAKDOWN=======")
        print(f"- Groceries: {category_counts["groceries"]}")
        print(f"- Clothing: {category_counts["clothing"]}")
        print(f"- Electronics: {category_counts["electronics"]}")
        print(f"- Tools: {category_counts["tools"]}")
        print(f"- Toys: {category_counts["toys"]}")
        print("================================")


class User:
    def __init__(self, inventory):
        self.user_list = []  # List of users who have registered
        self.inventory = inventory #Inheritance of inventory

    def save_user_credentials_to_json(self):
        """After the user register, it saves the user credentials to json file"""

        user_list_data = []  # Temporarily stores the users' data who have registered

        for user in self.user_list:
            user_credentials = {
                "username": user["username"],
                "password": user["password"],
            }
            user_list_data.append(user_credentials)

        with open(user_database_path, "w") as file:
            json.dump(user_list_data, file, indent=4)

    def load_user_credentials_from_json(self):
        """Load all the users' credentials who have registered"""

        try:
            with open(user_database_path, "r") as file:
                user_data = json.load(file)

            for user in user_data:
                user_credentials = {"username": user["username"], "password": user["password"]}
                self.user_list.append(user_credentials)

        except FileNotFoundError:
            print("Starting Fresh!")
    
    def save_user(self, new_registered_user):
        """After the register, save the user to inventory_database"""

        with open(inventory_database_path, "r") as file:
            data = json.load(file)
        
        temp_all_user_inventory = [] #Temporarily store all the user's inventory

        for user in data:
            user_info = {"username": user["username"], "inventory": user["inventory"]}
            temp_all_user_inventory.append(user_info)
        
        self.inventory.user_inventory_list.append(new_registered_user) #Register user inventory products -- Inventory()
        temp_all_user_inventory.append(new_registered_user)

        with open(inventory_database_path, "w") as file:
            json.dump(temp_all_user_inventory, file, indent = 4)       

    def load_users(self):
        try:
            with open(inventory_database_path, "r") as file:
                user_list = json.load(file)
        
            for user in user_list:
                temp_user_inventory = {"username": user["username"], "inventory": user["inventory"]}
                self.inventory.user_inventory_list.append(temp_user_inventory)

        except FileNotFoundError:
            print("Starting Fresh")

    def register(self):
        """Register a user with username and password"""

        print("\n=======REGISTER=======")
        username = input("Enter username: ").lower()
        password = input("Enter password: ")

        # Check if user exist
        for user in self.user_list:
            if username == user["username"]:
                print(f"\n{username.title()} is already taken")
                return

        # Check if password is strong
        if len(password) < 8:
            print("Password too weak!\n")
            return

        user_credentials = {"username": username, "password": password}
        self.user_list.append(user_credentials) #Save the user_credentials to user list -- User()

        print("\nRegistered sucessfully!")
        print(f"Welcome {username.title()}")

        user_inventory = {"username": username, "inventory": []}
        self.save_user(user_inventory)

    def login(self):
        """Prompt the user to login"""
        
        print("\n=======LOGIN=======")
        username = input("Enter username: ").lower()
        password = input("Enter password: ")

        # Find the username in user_database
        for user in self.user_list:
            if username == user["username"]:
                current_user = user #Temporarily store the user to later check for password
                break
        else:
            print(f"\n{username.title()} is not registered yet!")
            return None

        # Check if password match
        if password != current_user["password"]:
            print("\nPassword don't match!")
            return None

        #Switch the current user to Inventory_Database for later editing e.g., Add products and Remove products
        for user in self.inventory.user_inventory_list:
            if username == user["username"]:
                self.inventory.current_user = user
                break

        print("\nLogin Successfully!")
        return self.inventory.current_user

    def add_product(self):
        """Let a user add a product with product information"""

        product_name = input("\nEnter product name: ")
        product_id = validate_integer("Enter product ID: ")
        product_quantity = validate_integer("Enter product quantity: ")
        product_price = validate_integer("Enter product price (Per Item): ")
        product_category = get_product_category(self)

        # Check if product ID exists
        for product in self.inventory.current_user_inventory:
            if product.product_id == product_id:
                print(f"\nProduct with Product#{product_id} is already added!\n")
                return

        product = Products(product_name, product_id, product_quantity, product_price, product_category)

        self.inventory.current_user_inventory.append(product)
        print(f"{product_name.title()} has been added successfully!\n")

    def remove_product(self):
        """Let a user remove a specific product in an inventory"""

        search_id = validate_integer("Enter the product's ID you want to remove: ")

        for product in self.inventory.current_user_inventory:
            if product.product_id == search_id:
                self.inventory.current_user_inventory.remove(product)
                print(f"Removed {product.product_name.title()} successfully!")
                return
        else:
            print(f"Product with ID#{search_id} can't be found!")
            return

    def edit_product(self):
        """Let a user edit a product information -- even all information at once"""
        
        search_id = validate_integer("Enter the product's ID you want to edit: ")

        for product in self.inventory.current_user_inventory:
            if product.product_id == search_id:
                current_product = product
                break
        else:
            print(f"Product with ID#{search_id} can't be found!\n")
            return

        edit_choice = get_edit_area()

        if edit_choice == 1:  # Edit product's name
            new_product_name = input("Enter new product name: ")
            current_product.product_name = new_product_name
            print(
                f"Product name has been successfully updated! -- {new_product_name.title()}"
            )
            return

        if edit_choice == 2:  # Edit product's quantity
            new_product_quantity = validate_integer("Enter new product quantity: ")
            current_product.product_quantity = new_product_quantity
            print(
                f"Product quantity has been successfully updated! -- {new_product_quantity}"
            )
            return

        if edit_choice == 3:  # Edit product's price
            new_product_price = validate_integer("Enter new product price (Per Item): ")
            current_product.product_price = new_product_price
            print(
                f"Product price has been successfully updated! -- {new_product_price}"
            )
            return

        if edit_choice == 4:  # Edit product's category
            new_product_category = get_product_category(self)

            current_product.product_category = new_product_category
            print(
                f"Product category has been successfully updated! -- {new_product_category.title()}"
            )
            return

        if edit_choice == 5:  # Update all product's information
            new_product_name = input("Enter new product name: ")
            new_product_quantity = validate_integer("Enter new product quantity: ")
            new_product_price = validate_integer("Enter new product price: ")
            new_product_category = get_product_category(self)

            current_product.product_name = new_product_name
            current_product.product_quantity = new_product_quantity
            current_product.product_price = new_product_price
            current_product.product_category = new_product_category

            print(f"Product with ID#{search_id} has been sucessfully updated!\n")