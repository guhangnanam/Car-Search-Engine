

class Vehicle:

    def __init__(self, make, model, year, mileage, horsepower, body_type):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage
        self.horsepower = horsepower
        self.body_type = body_type

    def display_info(self):
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Mileage: {self.mileage} miles")
        print(f"Horsepower: {self.horsepower} HP")
        print(f"Body Type: {self.body_type}")

