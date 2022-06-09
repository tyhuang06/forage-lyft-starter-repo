import unittest

from tires.carrigan_tires import CarriganTires
from tires.octoprime_tires import OctoprimeTires


class TestCarriganTires(unittest.TestCase):
    def test_needs_service(self):
        wear_sensors = [0, 0.1, 0.6, 0.9]

        tires = CarriganTires(wear_sensors)
        self.assertTrue(tires.needs_service())

    def test_not_need_service(self):
        wear_sensors = [0, 0.1, 0.6, 0.4]

        tires = CarriganTires(wear_sensors)
        self.assertFalse(tires.needs_service())


class TestOctoprimeTires(unittest.TestCase):
    def test_needs_service(self):
        wear_sensors = [0.8, 0.9, 0.4, 0.9]

        tires = OctoprimeTires(wear_sensors)
        self.assertTrue(tires.needs_service())

    def test_not_need_service(self):
        wear_sensors = [0, 0.1, 0.6, 0.4]

        tires = OctoprimeTires(wear_sensors)
        self.assertFalse(tires.needs_service())