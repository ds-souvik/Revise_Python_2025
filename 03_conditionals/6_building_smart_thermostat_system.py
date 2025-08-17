"""You're building a smart thermostat alert system

1. If the device_status is 'active' 
    a. And temperature > 35 --> Warn: 'High Temperature' 
    B. Else 'Temperature Normal' 
2. If device is off --> 'Device is offline' """

device_status = input("What is the current device status?(Active/ Off): ")

if device_status.lower() == 'active':
    device_temperature = int(input("What is the device temperature?: "))
    if device_temperature > 35:
        print("High Temperature")
    else:
        print("Temperature Normal")
elif device_status.lower() == 'off':
    print("Device is offline")
else:
    print("Invalid status input. Please try again..")