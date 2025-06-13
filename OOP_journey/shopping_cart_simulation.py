from shopping_cart_simulation_functions import *

class Product:
    def __init__(self, item_name, item_id, item_price, item_size, item_stock):
        self.item_name = item_name
        self.item_price = item_price
        self.item_size = item_size
        self.item_stock = item_stock
        self.item_id = item_id

    def show_product_info(self):
        print("==============================")
        print("         ITEM INFO")
        print(f"Item Name: {self.item_name}")
        print(f"Item ID: {self.item_id}")
        print(f"Item Price: {self.item_price}")
        print(f"Item Size: {self.item_size}")
        print(f"Item Stock: {self.item_stock}")
        print("==============================")

class CartItem(Product):
    def __init__(self, item_name, item_id, item_price, item_size, item_stock):
        super().__init__(item_name, item_id, item_price, item_size, item_stock)

class Cart:
    def __init__(self):
        self.items = []

    def add_to_cart(self, cart_item):
        self.items.append(cart_item)

    def view_cart(self):
        if not self.items:
            print("Your cart is empty!\n")
            return

        total_cost = 0
        print("===============================")
        print("         YOUR CART")
        for item in self.items:
            item_name = item.item_name
            item_price = item.item_price
            quantity = item.item_stock
            subtotal = item_price * quantity
            total_cost += subtotal
            print(f"{quantity}x {item_name} - ₱{item_price} each = ₱{subtotal}")

        print(f"Your total cost: {total_cost}")
        print("===============================")

    def remove_from_cart(self, item):
        self.items.remove(item)


class User:
    def __init__(self, add, remove, view, checkouts):
        self.add = add
        self.remove = remove
        self.view = view
        self.checkout = checkouts

class Store(Product):
    def __init__(self, item_name, item_id, item_price, item_size, item_stock):
        super().__init__(item_name, item_id, item_price, item_size, item_stock)

def product_creation():
    product_one = Product("Laptop", 101, 2000, 300, 5)
    product_two = Product("Mouse", 102, 1000, 50, 7)
    product_three = Product("Keyboard", 103, 3000, 200, 9)
    product_four = Product("Charger", 104,  5000, 100, 4)
    product_list = [product_one, product_two, product_three, product_four]
    return product_list

def view_product_info(products):
    view_product_id = validate_integer("Enter Product ID you want to VIEW: ")
    for product in products:
        if view_product_id == product.item_id:
            product.show_product_info()
            break
    else:
        print(f"{view_product_id} can't be found!")
        return

def add_product_to_cart(products, cart):
    add_product_id = validate_integer("Enter Product ID: ")
    product_qty = validate_integer("Enter Quanity: ")

    for product in products:
        if add_product_id != product.item_id:
            continue

        if 0 <= product.item_stock < product_qty:
            print(f"{product.item_name} don't have enough stock!")
            return

        for item in cart.items:
            if item.item_id == add_product_id:
                item.item_stock += product_qty
                product.item_stock -= product_qty
                print(f"{product_qty}x more {item.item_name} has been added to cart!")
                return

        cart_item = CartItem(product.item_name, product.item_id, product.item_price, product.item_size, product_qty)
        cart.add_to_cart(cart_item)
        product.item_stock -= product_qty
        print(f"{product_qty}x {product.item_name} has been added to cart!")
        return

    print(f"Product with Product ID#{add_product_id} is not available")

def remove_product_from_cart(cart, products):
    if not cart.items:
        print("Your cart is empty!\n")
        return

    user_item = input("Enter the name of item you want to remove: ")
    remove_qty = validate_integer("Enter how many you want to remove: ")


    for item in cart.items:
        if item.item_name.lower() != user_item.lower():
            continue

        #Check if the quantity user wants to remove exceed item_stock in Cart
        if remove_qty > item.item_stock:
            print(f"{item.item_name} has only {item.item_stock} in your cart!\n")
            return

        #Remove the item_cart in Cart class and update the stock in Products
        if item.item_stock > remove_qty:
            item.item_stock -= remove_qty
            for product in products:
                if product.item_id == item.item_id:
                    product.item_stock += remove_qty
            print(f"{remove_qty}x of {item.item_name} has been removed from your cart!")
            cart.view_cart()
            break
        else:
            cart.remove_from_cart(item)
            for product in products:
                if product.item_id == item.item_id:
                    product.item_stock += remove_qty
            print(f"{item.item_name} has been removed from your cart!")
            cart.view_cart()
            break

    else:
        print(f"{user_item} is not in your cart!")
        return

def checkout(cart):
    if not cart.items:
        print("Your cart is empty and there is nothing to checkout!\n")
        return

    cart.view_cart()
    while True:
        checkout_choice = input("Do you want to proceed with checkout?\n"
                            "(YES or NO): ").upper()
        if checkout_choice == "YES":
            cart.items = []
            print("Checkout Confirmed. Thank You!")
            return
        elif checkout_choice == "NO":
            return
        else:
            print("Please enter YES or NO only!\n")

def main():
    products = product_creation()
    cart = Cart()
    user_continue = True
    while user_continue:
        print("===============================\n"
                "    WELCOME TO PASEK SHOP\n"
                "===============================")
        print("AVAILABLE PRODUCTS:")
        number = 1
        for product in products:
            print(f"#10{number}: {product.item_name} - {product.item_price} - (Stock: {product.item_stock})")
            number += 1
        print()

        choice = user_option()
        if choice == 1:
            view_product_info(products)
        if choice == 2:
            add_product_to_cart(products, cart)
        if choice == 3:
            cart.view_cart()
        if choice == 4:
            remove_product_from_cart(cart, products)
        if choice == 5:
            checkout(cart)
        if choice == 6:
            return
        user_continue = user_cont()

main()