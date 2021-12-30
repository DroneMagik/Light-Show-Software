import basic_movements_functions, drone_class
#from __future__ import print_function

# Initialize/ connect vehicle
vehicle = basic_movements_functions.connect_drone()

# Initialize drone.
drone = drone_class.Drone(vehicle)


# Arm drone
drone.movements.arm()

#takeoff to 100m altitude
drone.movements.take_off_to_alt(100)

# return to launch
drone.movements.returnToLaunch()


