import basic_movements_functions as basic_movements


class DroneMovements:
    def __init__(self, vehicle):
        self.vehicle = vehicle
    def arm(self):
        basic_movements.arm(self.vehicle)
    
    def take_off_to_alt(self, altitude):
        basic_movements.take_off_to_alt(self.vehicle, altitude)
    
    def returnToLaunch(self):
        basic_movements.returnToLaunch(self.vehicle)


