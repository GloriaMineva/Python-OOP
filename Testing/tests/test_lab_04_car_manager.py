from lab_04_car_manager import Car

from unittest import TestCase, main


class TestCar(TestCase):
    def setUp(self):
        self.car = Car('bmw', 'a30', 10, 500)

    def test_init(self):
        self.assertEqual('bmw', self.car.make)
        self.assertEqual('a30', self.car.model)
        self.assertEqual(10, self.car.fuel_consumption)
        self.assertEqual(500, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_make_setter_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = ''

        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_model_setter_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = ''

        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_fuel_consumption_setter_zero_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = 0

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_consumption_setter_negative_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = -1

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_capacity_zero_setter_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = 0

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_fuel_capacity_negative_setter_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = -1

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_fuel_amount_negative_setter_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -60

        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_refuel_raises(self):
        self.assertEqual(0, self.car.fuel_amount)
        with self.assertRaises(Exception) as ex:
            self.car.refuel(0)

        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))
        self.assertEqual(0, self.car.fuel_amount)

        self.assertEqual(0, self.car.fuel_amount)
        with self.assertRaises(Exception) as ex:
            self.car.refuel(-1)

        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))
        self.assertEqual(0, self.car.fuel_amount)

    def test_refuel_success(self):
        self.assertEqual(0, self.car.fuel_amount)
        self.car.refuel(5)
        self.assertEqual(5, self.car.fuel_amount)
        self.car.refuel(2)
        self.assertEqual(7, self.car.fuel_amount)

    def test_drive_raises(self):
        self.assertEqual(0, self.car.fuel_amount)
        with self.assertRaises(Exception) as ex:
            self.car.drive(5)

        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))
        self.assertEqual(0, self.car.fuel_amount)

    def test_drive_success(self):
        self.car.fuel_amount = 100
        self.car.drive(100)

        self.assertEqual(90, self.car.fuel_amount)



if __name__ == '__main__':
    main()
