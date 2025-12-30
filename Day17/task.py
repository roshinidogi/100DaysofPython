class User:
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username

user1 = User(1, "Rosh")
print(user1.username + " " + str(user1.user_id))
user2 = User(2, "Jaan")
print(user2.username + " " + str(user2.user_id))
user3 = User(3, "Sravs")
print(user3.username + " " + str(user3.user_id))