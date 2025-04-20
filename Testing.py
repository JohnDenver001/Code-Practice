from calculator_functions import *

user_name = input("Enter Your Name: ")
print("Hello", user_name)

continue_calculating = True
while continue_calculating:

    print()
    print("Please Select Operation You Want To Use,", user_name)
    print("===========================================")
    print("         Enter 1 for Addition")
    print("         Enter 2 for Subtraction")
    print("         Enter 3 for Multiplication")
    print("         Enter 4 for  Division")
    print("===========================================")

    user_input = get_user_operation()

    if user_input == 1:
        count = None
        while count is None:
            count = is_count_valid("Add")
        inputs = [is_number_valid(f"Enter Number {1 + i}: ") for i in range(count)]
        result = add(*inputs)
        print("The Result is:", result)

    if user_input == 2:
        count = None
        while count is None:
            count = is_count_valid("Subtract")
        inputs = [is_number_valid(f"Enter Number {1 + i}: ") for i in range(count)]
        result = sub(*inputs)
        print("The Result is: ", result)

    if user_input == 3:
        count = None
        while count is None:
            count = is_count_valid("Multiply")
        inputs = [is_number_valid(f"Enter Number {1 + i}: ") for i in range(count)]
        result = mult(*inputs)
        print("The Result is: ", result)

    if user_input == 4:
        print("Please take note that you can only enter two number at once.")
        is_div_valid = False
        while not is_div_valid:
            try:
                numerator = float(input("Please Enter the Numerator: "))
                result = div(numerator, denominator_input_validation())
                print("The Result is:", result)
                is_div_valid = True
            except ValueError:
                print("Please Enter Number Only!")
                print()
    continue_calculating = cont_calculating()