class Citizen:
    """
    In this class, we define attributes & methods for a citizen
    """
    counter = 0
    def __init__(self, name, age, gender, aadhar):
        self.name = name
        self.age = age
        self.gender = gender
        self.aadhar = aadhar
    @classmethod
    def count_citizens(cls):
        """
        Calculate the number objects that gets created from this class
        """
        cls.counter = cls.counter + 1
    def add_citizen(self):
        pass
    def remove_citizen(self):
        pass
    def is_adult(self):
        if age >= 18:
            return True
        else:
            return False
