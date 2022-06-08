from servicable import Servicable


class Car(Servicable):
    def __init__(self, engine, battery):
        self.battery = battery
        self.engine = engine

    def needs_service(self):
        return self.battery.needs_service() or self.engine.needs_service()
