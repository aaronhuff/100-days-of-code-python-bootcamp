class User:
    def __init__(self, name, username=None, password=None, email=None):
        self.name = name
        self.username = username
        self.password = password
        self.email = email
        self.followers = 0

    def add_follower(self):
        self.followers += 1

    def remove_follower(self):
        self.followers -= 1


aaron = User('Aaron')
for x in range(5):
    aaron.add_follower()
aaron.remove_follower()
print(aaron.followers)
