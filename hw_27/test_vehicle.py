# test_vehicle.py
import pytest
from vehicle import Vehicle, ElectricVehicle


def test_vehicle_init():
    vehicle = Vehicle("Toyota", "Camry", 2022)
    assert vehicle.brand == "Toyota"
    assert vehicle.model == "Camry"
    assert vehicle.year == 2022
    assert vehicle.gaz_tank_size == 45
    assert vehicle.fuel_level == 0


def test_vehicle_fuel_up():
    vehicle = Vehicle("Honda", "Civic", 2020)
    assert vehicle.fuel_up == "Gas tank is now full or can move."
    assert vehicle.fuel_level == 45


def test_vehicle_drive():
    vehicle = Vehicle("Ford", "Mustang", 2018)
    assert vehicle.drive == "The Mustang is now driving."


def test_electric_vehicle_init():
    ev = ElectricVehicle("Tesla", "Model S", 2021)
    assert ev.brand == "Tesla"
    assert ev.model == "Model S"
    assert ev.year == 2021
    assert ev.battery_size == 85
    assert ev.charge_level == 0


def test_electric_vehicle_charge():
    ev = ElectricVehicle("Nissan", "Leaf", 2019)
    assert ev.charge == "The vehicle is now charged."
    assert ev.charge_level == 100


def test_electric_vehicle_fuel_up():
    ev = ElectricVehicle("Chevrolet", "Bolt", 2020)
    assert ev.fuel_up == "This vehicle has no fuel tank!"
