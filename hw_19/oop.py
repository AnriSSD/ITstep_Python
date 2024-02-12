class Car:
    def __new__(cls, *args, **kwargs):
        print("Creating instance using __new__")
        instance = super().__new__(cls)
        return instance

    def __init__(self, brand, model, year):
        print("Initializing instance using __init__")
        self.__brand = brand
        self.__model = model
        self.__year = year

    def set_brand(self, brand):
        if not isinstance(brand, str):
            raise TypeError("Brand must be a string")
        self.__brand = brand

    def set_model(self, model):
        if not isinstance(model, str):
            raise TypeError("Model must be a string")
        self.__model = model

    def set_year(self, year):
        if not isinstance(year, int):
            raise TypeError("Year must be an integer")
        self.__year = year

    def get_brand(self):
        return self.__brand

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year


car = Car("Toyota", "Camry", 2018)
print(car.get_brand())
print(car.get_model())
print(car.get_year())

# atributebis shecvla
car.set_brand("Toyota")
car.set_model("Prius")
car.set_year(2018)
print(car.get_brand())
print(car.get_model())
print(car.get_year())

try:
    car.set_year("2018")
except TypeError as e:
    print(e)
