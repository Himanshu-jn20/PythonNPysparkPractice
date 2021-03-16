class Vehicle:
    def general_usage(self):
        print ('Vehicle')


class Car(Vehicle):
    def __init__(self):
        self.wheels=4
        self.has_roof=True

    def specific_usage(self):
        print('Long Drive/Safe/Accommodate 4 People')


class Bike(Vehicle):
    def __init__(self):
        self.wheels=2
        self.has_roof=False

    def specific_usage(self):
        self.general_usage()
        print('Cool/Not Safe/Racing')

tesla=Car()
tesla.general_usage()
tesla.specific_usage()

avenger=Bike()
avenger.specific_usage()
print(f'Avengers wheels - {avenger.wheels}')

print(issubclass(Car,Bike))
print(isinstance(avenger,Bike))