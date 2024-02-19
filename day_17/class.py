class User: ##first letter as capital it is known as Pascal Case.

    def __init__(self,id,name):  #constructor
        self.id = id
        self.username = name
        self.follower = 0        #deafult value initialised
        self.following = 0

    def follow(self,user):
        self.following += 1
        user.follower += 1




user_1 = User('101',"manas")
# user_1.id = '001'
# user_1.username = "manas"
# print(user_1.username)
user_2 = User("066","angela")
user_1.follow(user_2)
print(user_1.following, user_1.follower)
print(user_2.following,user_2.follower)





