

class Vehicle:

    def __init__(self, make, model, yearFrom, yearTo, trim, horsepower, body_type):
        self.make = make
        self.model = model
        self.yearFrom = (yearFrom)
        self.yearTo = (yearTo)
        self.trim = trim
        self.horsepower = (horsepower)
        self.body_type = body_type

    def display_info(self):
        return (
            f"Make: {self.make}\n"
            f"Model: {self.model}\n"
            f"Year From: {self.yearFrom}\n"
            f"Year To: {self.yearTo}\n"
            f"Trim: {self.trim}\n"
            f"Horsepower: {self.horsepower} HP\n"
            f"Body Type: {self.body_type}\n"
        )

