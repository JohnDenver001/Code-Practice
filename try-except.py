def is_count_valid():
    try:
        count = int(input("Enter How Many Numbers You Want to Add: "))
        if count > 0:
            print("True")
            return True
        else:
            print("False")
            return False
    except ValueError:
        print("Please Input Numbers Only")
        return False
is_count_valid()