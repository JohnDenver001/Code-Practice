class User:
    def __init__(self, firstName, lastName, likesCount, friendsName):
        self.firstName = firstName
        self.lastName = lastName
        self.likesCount = likesCount
        self.friendsName = friendsName

    def introduce_user(self):
        print(f"Hello! I am {self.firstName} {self.lastName}")

    def full_profile(self):
        print("USER FULL PROFILE:")
        print(f"Full Name: {self.firstName} {self.lastName}")
        print(f"Likes Count: {self.likesCount}")
        print("USER FRIENDS LIST:")
        print("\n".join(self.friendsName))


user_first_name = input("Enter your first name: ")
user_last_name = input("Enter your last name: ")
user_likes_count = int(input("Enter your likes count: "))
friends_count = int(input("Enter how many friends do you have: "))

user_friends_list = []
for i in range(friends_count):
    user_friends = (input(f"Enter your friend number {i + 1}'s name: "))
    user_friends_list.append(user_friends)

user_one = User(user_first_name, user_last_name, user_likes_count, user_friends_list)
print()
user_one.introduce_user()
print()
user_one.full_profile()