class User:
    """Stores and presents user profile information"""

    def __init__(self, first_name, last_name, password, account_age):
        """Initialize attributes to define a user"""
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.account_age = account_age
        self.login_attempts = 0

    def describe_user(self):
        """Summarizes the users account info"""
        print(f"The users name is {self.first_name.title()} " 
              f"{self.last_name.title()}, their password is {self.password} and" 
              f" they have had an account for {self.account_age} years")
        
    def greet_user(self):
        """Displays a personalized greeting to the user"""
        print(f"Hello {self.first_name.title()} {self.last_name.title()}." 
              " Welcome back to the site!")
        
    def increment_login_attempts(self):
        """Counts login attempts"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Resets login attempts to 0"""
        self.login_attempts = 0
        
user1 = User('Dowell', 'Gandy', 'password123', 7)

user1.increment_login_attempts()
print(user1.login_attempts)
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print(user1.login_attempts)
user1.reset_login_attempts()
print(user1.login_attempts)

