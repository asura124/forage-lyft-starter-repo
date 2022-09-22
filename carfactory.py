from datetime import datetime
from datetime import date
from typing import List
from car import Car
from engine.willoughby_engine import WilloughbyEngine
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from battery.nubbin_Battery import nubbinBattery
from battery.spindler_Battery import spindlerBattery
from tires.carrigan_tires import CarriganTires
from tires.octoprime_tires import OctoprimeTires

class carfactory():
    def create_calliope(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, tires_arr: List[int]):
        engine = CapuletEngine(current_mileage,last_service_mileage)
        battery = spindlerBattery(current_date,last_service_date)
        tire = CarriganTires(tires_arr)  #Assume Carrigan Tires for Calliope
        return Car(engine,battery,tire)

    def create_glissade(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, tires_arr: List[int]):
        engine = WilloughbyEngine(current_mileage,last_service_mileage)
        battery = spindlerBattery(current_date,last_service_date)
        tire = CarriganTires(tires_arr)  #Assume Carrigan Tires for Glissade
        return Car(engine,battery,tire)

    def create_palindrome(current_date: date, last_service_date: date, warning_light_on: bool, tires_arr: List[int]):
        engine = SternmanEngine(warning_light_on)
        battery = spindlerBattery(current_date,last_service_date)
        tire = CarriganTires(tires_arr)  #Assume Carrigan Tires for Palindrome
        return Car(engine,battery,tire)

    def create_rorschach(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, tires_arr: List[int]):
        engine = WilloughbyEngine(current_mileage,last_service_mileage)
        battery = nubbinBattery(current_date,last_service_date)
        tire = OctoprimeTires(tires_arr)  #Assume Octoprime Tires for rorschach
        return Car(engine,battery,tire)

    def create_thovex(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, tires_arr: List[int]):
        engine = CapuletEngine(current_mileage,last_service_mileage)
        battery = nubbinBattery(current_date,last_service_date)
        tire = OctoprimeTires(tires_arr)  #Assume Octoprime Tires for Thovex
        return Car(engine,battery,tire)