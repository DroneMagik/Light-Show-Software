import basic_movements_class

class Drone:
    def __init__(self, vehicle):
        self.vehicle = vehicle

        # Initialize movements class.
        self.movements = basic_movements_class.DroneMovements(self.vehicle)

        # ****Other subclasses to the superclass "Drone" will be initialized here***
