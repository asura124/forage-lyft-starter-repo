import unittest
from datetime import datetime

from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from battery.nubbin_Battery import nubbinBattery
from battery.spindler_Battery import spindlerBattery
from tires.carrigan_tires import CarriganTires
from tires.octoprime_tires import OctoprimeTires


class TestCalliope(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)

        battery = spindlerBattery(today, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)

        battery = spindlerBattery(today, last_service_date)
        self.assertFalse(battery.needs_service())

    def test_engine_should_be_serviced(self):
        current_mileage = 30001
        last_service_mileage = 0

        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_mileage = 30000
        last_service_mileage = 0

        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())
    
    def test_tire_should_be_serviced(self):
        tire_arr = [0,0.8,1.1,0.1]
        tire = CarriganTires(tire_arr)
        self.assertTrue(tire.needs_service())

    def test_tire_should_not_be_serviced(self):
        tire_arr = [0.1,0.1,0.1,0.1]
        tire = CarriganTires(tire_arr)
        self.assertFalse(tire.needs_service())

class TestGlissade(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)

        battery = spindlerBattery(today,last_service_date)
        self.assertTrue(battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)

        battery = spindlerBattery(today, last_service_date)
        self.assertFalse(battery.needs_service())

    def test_engine_should_be_serviced(self):
        current_mileage = 60001
        last_service_mileage = 0

        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_mileage = 60000
        last_service_mileage = 0

        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())

    def test_tire_should_be_serviced(self):
        tire_arr = [0,0.8,1.1,0.1]
        tire = CarriganTires(tire_arr)
        self.assertTrue(tire.needs_service())

    def test_tire_should_not_be_serviced(self):
        tire_arr = [0.1,0.1,0.1,0.1]
        tire = CarriganTires(tire_arr)
        self.assertFalse(tire.needs_service())


class TestPalindrome(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)

        battery = spindlerBattery(today, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)

        battery = spindlerBattery(today, last_service_date)
        self.assertFalse(battery.needs_service())

    def test_engine_should_be_serviced(self):
        warning_light_is_on = True

        engine = SternmanEngine(warning_light_is_on)
        self.assertTrue(engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        warning_light_is_on = False

        engine = SternmanEngine(warning_light_is_on)
        self.assertFalse(engine.needs_service())

    def test_tire_should_be_serviced(self):
        tire_arr = [0,0.8,1.1,0.1]
        tire = CarriganTires(tire_arr)
        self.assertTrue(tire.needs_service())

    def test_tire_should_not_be_serviced(self):
        tire_arr = [0.1,0.1,0.1,0.1]
        tire = CarriganTires(tire_arr)
        self.assertFalse(tire.needs_service())


class TestRorschach(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)

        battery = nubbinBattery(today,last_service_date)
        self.assertTrue(battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)

        battery = nubbinBattery(today, last_service_date)
        self.assertFalse(battery.needs_service())

    def test_engine_should_be_serviced(self):
        current_mileage = 60001
        last_service_mileage = 0

        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_mileage = 60000
        last_service_mileage = 0

        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())

    def test_tire_should_be_serviced(self):
        tire_arr = [1,1,1,1]
        tire = OctoprimeTires(tire_arr)
        self.assertTrue(tire.needs_service())

    def test_tire_should_not_be_serviced(self):
        tire_arr = [0.1,0.1,0.1,0.1]
        tire = OctoprimeTires(tire_arr)
        self.assertFalse(tire.needs_service())


class TestThovex(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)

        battery = nubbinBattery(today, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)

        battery = nubbinBattery(today, last_service_date)
        self.assertFalse(battery.needs_service())

    def test_engine_should_be_serviced(self):
        current_mileage = 30001
        last_service_mileage = 0

        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_mileage = 30000
        last_service_mileage = 0

        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())

    def test_tire_should_be_serviced(self):
        tire_arr = [1,1,1,1]
        tire = OctoprimeTires(tire_arr)
        self.assertTrue(tire.needs_service())

    def test_tire_should_not_be_serviced(self):
        tire_arr = [0.1,0.1,0.1,0.1]
        tire = OctoprimeTires(tire_arr)
        self.assertFalse(tire.needs_service())

if __name__ == '__main__':
    unittest.main()
