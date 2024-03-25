from vehicle import Vehicle
import unittest


class TestVehicle(unittest.TestCase):
    def setUp(self):
        self.vehicle = Vehicle("Toyota", "Camry", 2022)

    def test_init(self):
        self.assertEqual(self.vehicle.brand, "Toyota")
        self.assertEqual(self.vehicle.model, "Camry")
        self.assertEqual(self.vehicle.year, 2022)
        self.assertEqual(self.vehicle.gaz_tank_size, 45)
        self.assertEqual(self.vehicle.fuel_level, 0)

    def test_fuel_up(self):
        self.assertEqual(self.vehicle.fuel_up, "Gas tank is now full or can move.")
        self.assertEqual(self.vehicle.fuel_level, 45)

    def test_drive(self):
        self.assertEqual(self.vehicle.drive, "The Camry is now driving.")

    def test_fuel_up_empty(self):
        self.vehicle.fuel_level = 0
        self.assertEqual(self.vehicle.fuel_up, "Gas tank is empty and can not move.")
        self.assertEqual(self.vehicle.fuel_level, 45)


if __name__ == "__main__":
    unittest.main()
