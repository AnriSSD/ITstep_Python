class Car:
    def __init__(self, brand, model, year):
        print("Initializing instance using __init__")
        self.__brand = brand
        self.__model = model
        self.__year = year

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, brand):
        if not isinstance(brand, str):
            raise TypeError("Brand must be a string")
        self.__brand = brand

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        if not isinstance(model, str):
            raise TypeError("Model must be a string")
        self.__model = model

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):
        if not isinstance(year, int):
            raise TypeError("Year must be an integer")
        self.__year = year

# Example usage
car = Car("Toyota", "Camry", 2022)
print(car.brand)  # Outputs: Toyota
print(car.model)  # Outputs: Camry
print(car.year)   # Outputs: 2022

# Changing attributes
car.brand = "Honda"
car.model = "Civic"
car.year = 2018
print(car.brand)  # Outputs: Honda
print(car.model)  # Outputs: Civic
print(car.year)   # Outputs: 2018

# Trying to set the year attribute to a non-integer will raise an error
try:
    car.year = "2018"
except TypeError as e:
    print(e) 