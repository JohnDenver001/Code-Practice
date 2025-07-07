def validate_integer(word):
    """This function checks if user input is integer and is valid"""

    while True:
        try:
            valid = int(input(word))
            if valid < 0:
                print("Negative number is not valid -- Try Again!\n")
            return valid
        except ValueError:
            print("Enter number only!\n")


def get_user_action():
    """This function display welcoming User and get
    their action Ex. Add items/Remove Items"""

    print("\n======WELCOME======")
    while True:
        user_action = validate_integer(
            "[1] Add Product\n"
            "[2] Remove Product\n"
            "[3] Edit Product\n"
            "[4] List Products\n"
            "[5] Show Stats\n"
            "[6] Save and Exit\n"
            "Choice: "
        )

        if 0 < user_action < 7:
            return user_action
        print("Enter number 1-6 only!\n")


def get_edit_area():
    """Gets the user input in what area
    the user wants to edit"""
    while True:
        edit_choice = validate_integer(
            "What do you want to edit?\n"
            "[1] Name\n"
            "[2] Quantity\n"
            "[3] Price\n"
            "[4] Category\n"
            "[5] All\n"
            "Choice: "
        )
        if 0 < edit_choice < 6:
            return edit_choice
        print("Enter number 1-5 only!\n")


def show_available_product_category(self):
    """Prints all available product category"""
    print("==LIST OF AVAILABLE PRODUCT CATEGORY==")

    for i in range(len(self.product_category_list)):  # Show available product category
        print(f"[{i + 1}] {self.product_category_list[i].title()}")
    print("======================================")
    return


def get_product_category(self):
    """Get the product category and check if it is available
    -- print available product category if not"""

    while True:
        product_category = input("Enter product category: ").lower()

        if product_category not in self.product_category_list:
            print(f"\n{product_category.title()} is not available in product category")
            show_available_product_category(self)
            continue
        return product_category
