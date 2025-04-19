# def is_count_valid():
#     try:
#         count = int(input("Enter How Many Numbers You Want to Add: "))
#         if count > 0:
#             return count
#         else:
#             print("Please Input Number greater than 0")
#             return None
#     except ValueError:
#         print("Please Input Numbers Only")
#         return None
#
# def is_number_valid(prompt):
#     valid = False
#     while not valid:
#         try:
#             number = int(input(prompt))
#             return number
#         except ValueError:
#             print("Please Enter Numbers Only!")
#
# count = None
# while count is None:
#     count = is_count_valid()
#     for i in range(count):
#         inputs = is_number_valid(f"Enter Number {i + 1}: ")
#

def cont_calculating():
    check = True
    while check:
        con = input("Do You Still Want To Cotinue? ").upper()
        if con == "YES":
            return True
        elif con == "NO":
            print("Thank You!")
            return False
        else:
            print("Please Enter YES or NO only!")

continue_calculating = True
while continue_calculating:
    continue_calculating = cont_calculating()

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
