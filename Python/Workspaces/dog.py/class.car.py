class Car:
    # A simple attempt to represent a car.
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's milage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, milage):
        """Set the odometer reading to the given value.
         reject thre change if it attempts to roll back the odometer.
         """
        if milage >= self.odometer_reading:
            self.odometer_reading = milage
        else:
            print("You can't turn back the odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading"""
        self.odometer_reading += miles


class ElectricCar(Car):
    """Represents aspect of car, specific to electric vehicles"""

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 75

    def describe_battery(self):
        # print a staement describing a battery
        print(f"This car has a {self.battery_size}-kWh battery.")

    def fill_gas_tank(self):
        # Electric cars don't have gas tanks
        print("this car doesnt need a gas tank!")


class Battery:
    # A simple attempt to model a battery for an electric vehicle

    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This Car has a {self.battery_size}-kWh battery.")    


'''my_tesla = ElectricCar('Tesla', 'Model S', 2021)

car2 = Car('Ford', 'Focus', 2018)
#print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()'''
car1 = Car('Toyota', 'Tundra', 2003)
print(car1.get_descriptive_name())
