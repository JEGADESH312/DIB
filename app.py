 
import time
from dronekit import connect, VehicleMode, LocationGlobalRelative,LocationGlobal
from rover import closeTopDoor, openTopDoor
from rover import initRover,getRoverStatus,DoorStatus,RoverClose
vehicle=any


def initVehicle(vehicleID):
    global vehicle
    # vehicleID="tcp:"+vehicleID
    vehicle = connect(vehicleID, wait_ready=True)
    print('Vehicle connected',"Connected!!!!!!!!!!!!!!!!!!!!!!!")

def getStatus():

    time.sleep(1)
    vehicledata={
        'Home Location':{
                    "Latitude":vehicle.location.global_relative_frame.lat,
                    "Longitude":vehicle.location.global_relative_frame.lon,
                    "Altitude":vehicle.location.global_relative_frame.alt
                    },
        # "GPS":vehicle.gps_0.num_sat,
        "Model":vehicle.mode.name,
        "Battery":vehicle.battery.level,
        "Armed":vehicle.armed
    } 
    print("-----------------------------Vehicle Status----------------------------------------")

    print('vehicle_data',vehicledata)
    time.sleep(5)






def arm_and_takeoff():

        print("Basic pre-arm checks")
        # Don't try to arm until autopilot is ready
        while not vehicle.is_armable:
            print(" Waiting for vehicle to initialise...")
            time.sleep(1)

        print("Arming motors")
        # Copter should arm in GUIDED mode
        vehicle.mode = VehicleMode("GUIDED")
        vehicle.armed = True

        # Confirm vehicle armed before attempting to take off
        while not vehicle.armed and not  vehicle.mode.name=="GUIDED":
            print(" Waiting for arming...")
            time.sleep(1)
        print('armed',"Armed!!!!!!!!!!!!! & Taking Off!!!!!!!!!!!!!!!!!!!!!!!!")
        return True


def takeOff(aTargetAltitude):
        vehicle.simple_takeoff(aTargetAltitude)  # Take off to target altitude
 
        while True:
            print(" Altitude: ", vehicle.location.global_relative_frame.alt)
            # Break and return from function just below target altitude.

            if vehicle.location.global_relative_frame.alt >= 20:
                print()
                print("Vehicle reached 20 meter altitude")
                DoorStatus("close")
                print()
                break
            time.sleep(5)

        while True:
            if vehicle.location.global_relative_frame.alt >= aTargetAltitude *0.95:
                print("Reached target altitude")
                break
            time.sleep(5)


def land():
    vehicle.mode=VehicleMode("LAND")

    print("Landing")
    while True:
            # Break and return from function just below target altitude.
        if vehicle.location.global_relative_frame.alt <= 20:
             DoorStatus("open")
             break

    while vehicle.armed != False:
        print("Waiting for landing")
        # insert the time delay taken by door closing
        time.sleep(2) 
    
    vehicle.close()
    time.sleep(1)

    DoorStatus("close")

 
initVehicle('tcp:192.168.1.231:5761')
initRover('tcp:127.0.0.1:14550')
getRoverStatus()
getStatus()



DoorStatus("open")

time.sleep(3)
 
if arm_and_takeoff():
        getStatus()
        print()
        print("Will ready to takeoff")
        takeOff(80)
        print()

else:
        print("Unable to open door,check it Else do manual")

print()
print('-----------------------------------------Hovering-----------------------------------------------------')
print()
time.sleep(20)
#close
 
land()
RoverClose()