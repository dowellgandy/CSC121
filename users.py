class User:
    """Stores and presents user profile information"""

    def __init__(self, first_name, last_name, password, account_age):
        """Initialize attributes to define a user"""
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.account_age = account_age

    def describe_user(self):
        """Summarizes the users account info"""
        print(f"The users name is {self.first_name.title()} " 
              f"{self.last_name.title()}, their password is {self.password} and" 
              f" they have had an account for {self.account_age} years")
        
    def greet_user(self):
        """Displays a personalized greeting to the user"""
        print(f"Hello {self.first_name.title()} {self.last_name.title()}." 
              " Welcome back to the site!")
        
user1 = User('Dowell', 'Gandy', 'password123', 7)
user2 = User('Jack', 'Smith', 'topsecret', 2)
user3 = User('Bob', 'Jobs', 'kalsdjfw23kasdf', 25)

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()
