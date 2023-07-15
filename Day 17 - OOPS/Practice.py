class User:

    # initializing attributes
    def __init__(self, user_id, username):
        # self is the object (User())
        self.id = user_id
        self.username = username
        # setting default value
        self.follower = 0
        self.following = 0

    def follow(self, user):
        # the (other, mentioned)user account gets 1 follower
        user.follower += 1
        # and we start following
        self.following = +1


# user_1.id = "001"
# user_1.username = "Hafsa"
user_1 = User("001", "Hafsa")
user_2 = User("002", "Nafisa")
user_1.follow(user_2)
print(user_1.follower)
print(user_1.following)
print(user_2.follower)
print(user_2.following)
