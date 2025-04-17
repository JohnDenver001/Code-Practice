def add(*number):
    total = 0
    for num in number:
        total += num
    return total

def sub(*number):
    total = number[0]
    for num in number:
        total -= num
    return total

def mult(*number):
    total = 1
    for num in number:
        total *= num
    return total

def div(numOne, numTwo):
    return numOne / numTwo

def isCountValid(count):
    if count > 0:
        is_count_valid = True
    else:
        is_count_valid = False

user_name = input("Enter Your Name: ")
print("Hello", user_name)
print()
print("Please Select Operation You Want To Use,", user_name)
print("===========================================")
print("         Enter 1 for Addition")
print("         Enter 2 for Subtraction")
print("         Enter 3 for Multiplication")
print("         Enter 4 for  Division")
print("===========================================")

isUserOperationInputValid = False
while not isUserOperationInputValid:
    try:
        user_input = int(input("Input: "))
        if user_input <= 0 or user_input >= 5:
            print("Please Enter Number 1-4 Only!")
            print()
        else:
            isUserOperationInputValid = True
    except ValueError:
        print("Please Input Number Only!")
        print()

continue_calculating = True
while continue_calculating:







    isCountValid = False
    if user_input == 1:
        add_numbers = []
        while not isCountValid:
            try:
                count = int(input("Enter How Many Number You Want to Add: "))
                if count > 0:
                    isCountValid = True
                    try:
                        for i in range(count):
                            inputs = int(input (f"Enter Number {i + 1}: "))
                            if inputs > 0:
                                add_numbers.append(inputs)
                                result = add(*add_numbers)
                        print("The Result is:", result)
                    except ValueError:
                        print("Please Enter Numbers Only!")
                else:
                    print()
                    print("Please Enter Positive Integer Only!")
                    print()
            except ValueError:
                print("Please Input Number Only!")


















    #
    # elif op == 2:
    #     count = int(input("Enter How Many Number You Want to Subtract: "))
    #     inputs = [float(input(f"Enter Number {i + 1}: ")) for i in range(count)]
    #
    #     if count or inputs == "":
    #         inputs = [float(input("Please Enter a Valid Number: ")) for i in range(count)]
    #         result = sub(*inputs)
    #         print("The Result is:", result)
    #     else:
    #         result = sub(*inputs)
    #         print("The Result is:", result)
    #
    # elif op == 3:
    #     count = int(input("Enter How Many Number You Want to Add: "))
    #     inputs = [float(input(f"Enter Number {i + 1}: ")) for i in range(count)]
    #
    #     if count and inputs == "":
    #         inputs = [float(input("Please Enter a Valid Number: ")) for i in range(count)]
    #         result = mult(*inputs)
    #         print("The Result is:", result)
    #     else:
    #         result = mult(*inputs)
    #         print("The Result is:", result)
    #
    # elif op == 4:
    #     numerator = float(input("Enter the Numerator: "))
    #     denominator = float(input("Enter the Denominator: "))
    #
    #     if numerator and denominator == "":
    #         numerator = float(input("Please Input Valid Numerator: "))
    #         denominator = float(input("Please Input Valid Denominator: "))
    #         if denominator != 0:
    #             result = div(numerator, denominator)
    #             print("The Result is: ", result)
    #         else:
    #             print("0 as Denominator is invalid")
    #     result = div(numerator, denominator)
    #     print("The Result is: ", result)
    # con = input("Do You Still Want To Cotinue? ").upper()
    # if con == "NO":
    #     check = False
    #
