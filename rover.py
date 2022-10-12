import time
from dronekit import connect, VehicleMode, LocationGlobalRelative,LocationGlobal
from pymavlink import mavutil

vehicle=any

def openTopDoor():
    print('----------------------------------')
    print("Top door is opening-(1900)")
    msg=vehicle.message_factory.command_long_encode(0,0,mavutil.mavlink.MAV_CMD_DO_SET_SERVO,
    0,10,1900,0,0,0,0,0)
    vehicle.send_mavlink(msg)
    
    return True



def closeTopDoor():
    print('----------------------------------')
    print("Top door is closing-(1100)")
    msg=vehicle.message_factory.command_long_encode(0,0,mavutil.mavlink.MAV_CMD_DO_SET_SERVO,
    0,10,1100,0,0,0,0,0)
    vehicle.send_mavlink(msg)
    time.sleep(3)

    return True




def initRover(vehicleID):
    global vehicle
    # vehicleID="tcp:"+vehicleID
    vehicle = connect(vehicleID, wait_ready=True)
    print('Rover Connected',"Connected!!!!!!!!!!!!!!!!!!!!!!!")

def getRoverStatus():

    time.sleep(1)
    vehicledata={
        'Rover Location':{
                    "Latitude":vehicle.location.global_relative_frame.lat,
                    "Longitude":vehicle.location.global_relative_frame.lon,
                    "Altitude":vehicle.location.global_relative_frame.alt
                    },
        # "GPS":vehicle.gps_0.num_sat,
        "Model":vehicle.mode.name,
        "Battery":vehicle.battery.level,
        "Armed":vehicle.armed
    } 
    print("-----------------------------Rover Status----------------------------------------")

    print('vehicle_data',vehicledata)
    time.sleep(5)




def DoorStatus(condition):
    if(condition =="open"):
        openTopDoor()
    elif(condition == "close"):
        closeTopDoor()
    else:
        print("Error")

def RoverClose():
    vehicle.close()
 
# initRover("")
# getRoverStatus()
# DoorStatus("close")



# vehicle.close()