from tires.tires import Tires


class OctoprimeTires(Tires):
    def __init__(self, wear_sensors):
        self.wear_sensors = wear_sensors

    def needs_service(self):
        return sum(self.wear_sensors) >= 3
