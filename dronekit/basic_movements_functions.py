# Imports
from __future__ import print_function

from dronekit import connect, VehicleMode, LocationGlobalRelative, LocationGlobal, Command
import time
import math
from pymavlink import mavutil
#Set up option parsing to get connection string
import argparse  


# connect drone
def connect_drone():
    ''' 
    TODO: Add doccumentation   
    '''
    parser = argparse.ArgumentParser(description='Demonstrates basic mission operations.')
    parser.add_argument('--connect', 
                   help="vehicle connection target string. If not specified, SITL automatically started and used.")
    args = parser.parse_args()

    connection_string = args.connect
    sitl = None


    #Start SITL if no connection string specified
    if not connection_string:
        import dronekit_sitl
        sitl = dronekit_sitl.start_default()
        connection_string = sitl.connection_string()


    # Connect to the Vehicle
    print('Connecting to vehicle on: %s' % connection_string)
    vehicle = connect(connection_string, wait_ready=True)
    return vehicle

# Arm drone
def arm(vehicle):
    ''' 
    TODO: Add doccumentation   
    '''
    print("Basic pre-arm checks")
    # Don't try to arm until autopilot is ready
    while not vehicle.is_armable:
        print(" Waiting for vehicle to initialise...")
        time.sleep(1)
    print("Arming motors")
    # Copter should arm in GUIDED mode
    vehicle.mode = VehicleMode("GUIDED")
    vehicle.armed = True

    while not vehicle.armed:      
        print(" Waiting for arming...")
        time.sleep(1)
    print("Drone Armed")
    

# Takeoff function
def take_off_to_alt(vehicle, altitude):
    ''' 
    TODO: Add doccumentation   
    '''
    print("Taking off! Target altitude: ".format(altitude))
    vehicle.simple_takeoff(altitude)
    while True:
        print("    Altitude: ", vehicle.location.global_relative_frame.alt)      
        if vehicle.location.global_relative_frame.alt>=altitude*0.95:
            print("------Reached target altitude--------")
            break
        time.sleep(1)

def returnToLaunch(vehicle):
    ''' 
    TODO: Add doccumentation   
    '''
    print('Returning to launch')
    vehicle.mode = VehicleMode("RTL")
    time.sleep(1)