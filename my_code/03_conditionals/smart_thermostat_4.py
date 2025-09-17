device_status = input("select between active/inactive: ")

if device_status == "active":
    temp = int(input("Enter temp: "))
    if temp > 35:
        print("Warn: 'High temperature alert!'")
    else:
        print("Temp normal")
else:
    print("Device is offline")