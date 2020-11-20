import unittest


class Vehicle:
    def __init__(self, wheels, make, model, year):
        super().__init__()
        self.wheels = wheels
        self.make = make
        self.model = model
        self.year = year
        self.mileage = 0

    def addMileage(self, mileage):
        if mileage <= 0:
            return
        self.mileage += mileage


class Car(Vehicle):
    def __init__(self, make, model, year):
        super().__init__(4, make, model, year)


class Motorcycle(Vehicle):
    def __init__(self, make, model, year):
        super().__init__(2, make, model, year)


class test(unittest.TestCase):
    def testVehicle(self):
        v = Vehicle(3, "makeA", "modelA", 1997)
        self.assertEqual(v.wheels, 3)
        self.assertEqual(v.make, "makeA")
        self.assertEqual(v.model, "modelA")
        self.assertEqual(v.year, 1997)
        v.addMileage(100)
        self.assertEqual(v.mileage, 100)

    def testCar(self):
        v = Car("makeA", "modelA", 1997)
        self.assertEqual(v.wheels, 4)
        self.assertEqual(v.make, "makeA")
        self.assertEqual(v.model, "modelA")
        self.assertEqual(v.year, 1997)

    def testMotorCycle(self):
        v = Motorcycle("makeA", "modelA", 1997)
        self.assertEqual(v.wheels, 2)
        self.assertEqual(v.make, "makeA")
        self.assertEqual(v.model, "modelA")
        self.assertEqual(v.year, 1997)

    def testMotorCycleMielage(self):
        v = Motorcycle("makeA", "modelA", 1997)
        v.addMileage(-19)
        self.assertEqual(v.mileage, 0)


if __name__ == '__main__':
    unittest.main(verbosity=2)
