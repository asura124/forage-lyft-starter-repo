from engine.engine import engine
from battery.battery import battery
from Serviceable import serivceable

class Car(serivceable):
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery

    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service()
