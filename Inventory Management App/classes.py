from helper_function import *
import json
import os

file_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "Inventory_Database.json"
)


class Products:
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
        self.inventory_products = []  # List of products that has been added
        self.product_category_list = [
            "groceries",
            "clothing",
            "electronics",
            "tools",
            "toys",
        ]  # List of available product category

    def save_data_to_json(self):
        """Save the data's added by user"""
        data = []
        for product in self.inventory_products:
            product_information = {
                "product_name": product.product_name,
                "product_id": product.product_id,
                "product_quantity": product.product_quantity,
                "product_price": product.product_price,
                "product_category": product.product_category,
            }
            data.append(product_information)

        with open(file_path, "w") as file:
            json.dump(data, file, indent=4)

    def load_data_from_json(self):
        """Check if there is existing file for database, if yes - load it, else - Raise print Error"""

        try:
            with open(file_path, "r") as file:
                data = json.load(file)

            for product in data:
                product_information = Products(
                    product_name=product["product_name"],
                    product_id=product["product_id"],
                    product_quantity=product["product_quantity"],
                    product_price=product["product_price"],
                    product_category=product["product_category"],
                )
                self.inventory_products.append(product_information)

        except FileNotFoundError:
            print("File not found! -- Starting Fresh")

    def add_product(self):
        """Let a user add a product with product information"""

        product_name = input("\nEnter product name: ")
        product_id = validate_integer("Enter product ID: ")
        product_quantity = validate_integer("Enter product quantity: ")
        product_price = validate_integer("Enter product price (Per Item): ")
        product_category = get_product_category(self)

        # Check if product ID exists
        for product in self.inventory_products:
            if product.product_id == product_id:
                print(f"\nProduct with Product#{product_id} is already added!\n")
                return

        product = Products(
            product_name, product_id, product_quantity, product_price, product_category
        )

        self.inventory_products.append(product)
        print(f"{product_name.title()} has been added successfully!\n")

    def remove_product(self):
        """Let a user remove a specific product in an inventory"""

        search_id = validate_integer("Enter the product's ID you want to remove: ")

        for product in self.inventory_products:
            if product.product_id == search_id:
                self.inventory_products.remove(product)
                print(f"Removed {product.product_name.title()} sucessfully!")
                return
        else:
            print(f"Product with ID#{search_id} can't be found!")
            return

    def edit_product(self):
        """Let a user edit a product information -- even all information at once"""
        search_id = validate_integer("Enter the product's ID you want to edit: ")

        for product in self.inventory_products:
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

    def list_products(self):
        print("==========================================")
        print("             LIST OF PRODUCTS")
        print("===========================================")
        print("    Name     |  ID  | Quantity | Price | Category")

        for i in range(len(self.inventory_products)):
            print(
                f"[{i + 1}]: {self.inventory_products[i].product_name}  | {self.inventory_products[i].product_id} |     {self.inventory_products[i].product_quantity}     | {self.inventory_products[i].product_price} | {self.inventory_products[i].product_category.title()}"
            )

    def show_stats(self):
        """Shows the current status of user's inventory and shows the breakdown of products category"""
        total_products = len(self.inventory_products)
        total_quantity = 0
        total_value = 0
        category_counts = {
            "groceries": 0,
            "clothing": 0,
            "electronics": 0,
            "tools": 0,
            "toys": 0,
        }

        for product in self.inventory_products:
            total_quantity += product.product_quantity
            total_value += product.product_quantity * product.product_price

            if product.product_category in category_counts:
                category_counts[product.product_category] += 1

        print("======INVENTORY STATS======")
        print(f"Total Products: {total_products}")
        print(f"Total Quantity: {total_quantity}")
        print(f"Total Value: {total_value}\n")
        print("Category Breakdown:")
        print(f"- Groceries: {category_counts["groceries"]}")
        print(f"- Clothing: {category_counts["clothing"]}")
        print(f"- Electronics: {category_counts["electronics"]}")
        print(f"- Tools: {category_counts["tools"]}")
        print(f"- Toys: {category_counts["toys"]}")
