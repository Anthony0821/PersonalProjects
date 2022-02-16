class Dog:
    """A simple attempt to model a dog."""
    def _init_(self, name, age):
        """initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command"""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate a dog rolling over in response to a command"""
        print(f"{self.name} rolled over!")


my_dog = Dog('Ruby', 1)
print(f"My dog''s name is {my_dog.name}.")
print(f"my dog is {my_dog.age} years old")
