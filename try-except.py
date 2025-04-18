def is_count_valid():
    try:
        count = int(input("Enter How Many Numbers You Want to Add: "))
        if count > 0:
            return count
        else:
            print("Please Input Number greater than 0")
            return None
    except ValueError:
        print("Please Input Numbers Only")
        return None

def is_number_valid(prompt):
    valid = False
    while not valid:
        try:
            number = int(input(prompt))
            return number
        except ValueError:
            print("Please Enter Numbers Only!")

count = None
while count is None:
    count = is_count_valid()
    for i in range(count):
        inputs = is_number_valid(f"Enter Number {i + 1}: ")

