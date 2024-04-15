class Employee:
    """Stores and edits employee salary information"""

    def __init__(self, first_name, last_name, salary):
        """Stores employee salary information"""
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def give_raise(self, raze=5000):
        """Adds default or custom raise amount to employee salary"""
        self.salary = self.salary + raze

