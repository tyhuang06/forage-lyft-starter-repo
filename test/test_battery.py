import unittest
from datetime import datetime

from battery.nubbinBattery import NubbinBattery
from battery.spindlerBattery import SpindlerBattery


class TestSpindlerBattery(unittest.TestCase):
    def test_needs_service(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)

        battery = SpindlerBattery(today, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_not_need_service(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 2)

        battery = SpindlerBattery(today, last_service_date)
        self.assertFalse(battery.needs_service())


class TestNubbinBattery(unittest.TestCase):
    def test_needs_service(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)

        battery = NubbinBattery(today, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_not_need_service(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)

        battery = NubbinBattery(today, last_service_date)
        self.assertFalse(battery.needs_service())
