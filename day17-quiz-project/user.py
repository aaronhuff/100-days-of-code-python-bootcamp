class User:
    def __init__(self, name, email=None):
        self.name = name
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
print(f'Followers: {aaron.followers}')
