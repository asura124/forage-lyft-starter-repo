from datetime import datetime
from datetime import date 
from car import Car
from engine.willoughby_engine import WilloughbyEngine
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from battery.nubbin_Battery import nubbinBattery
from battery.spindler_Battery import spindlerBattery

class carfactory():
    def create_calliope(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        engine = CapuletEngine(current_mileage,last_service_mileage)
        battery = spindlerBattery(current_date,last_service_date)
        return Car(engine,battery)

    def create_glissade(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        engine = WilloughbyEngine(current_mileage,last_service_mileage)
        battery = spindlerBattery(current_date,last_service_date)
        return Car(engine,battery)

    def create_palindrome(current_date: date, last_service_date: date, warning_light_on: bool):
        engine = SternmanEngine(warning_light_on)
        battery = spindlerBattery(current_date,last_service_date)
        return Car(engine,battery)

    def create_rorschach(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        engine = WilloughbyEngine(current_mileage,last_service_mileage)
        battery = nubbinBattery(current_date,last_service_date)
        return Car(engine,battery)

    def create_thovex(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        engine = CapuletEngine(current_mileage,last_service_mileage)
        battery = nubbinBattery(current_date,last_service_date)
        return Car(engine,battery)