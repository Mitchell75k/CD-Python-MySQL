class User:
    # class attributes get defined in the class BEFORE the constructor if you want to use them in the constructor, or edit them for all instances
    def __init__(self, fname,lname, email, age): #this is the constructor, and only refers to the instances created from the class
        self.fname = fname
        self.lname = lname
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_pts=0

    def display_info(self):
        print(f"Name: {self.fname} {self.lname}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Rewards Member: {self.is_rewards_member}")
        print(f"Gold Card Points: {self.gold_card_pts}")
        return self

    def enroll(self):
        if self.is_rewards_member == False:
            self.is_rewards_member = True
            self.gold_card_pts += 200
        else:
            print("User is already a member.")
        return self #this is the key to chaining methods
    
    def spend_pts(self,amount):
        if self.gold_card_pts > amount:
            self.gold_card_pts -= amount
            print(f"You have spent {amount} points. You have {self.gold_card_pts} points left, thanks for shopping!.")
        else:
            print("You do not have enough points to spend.")
        return self #this will return the remaining points to the user after spending them
    

user1 = User("John", "Smith", 'Jsmith@gmail.com', 25)
user1.enroll().spend_pts(50).display_info().enroll()


user2 = User("Jane", "Doe", "JDoe@gmail.com", 40)
user2.enroll().spend_pts(80).display_info().spend_pts(3000)


user3 = User("Bob", "Smith", "BSmith@gmail.com", 21)
user3.display_info()

