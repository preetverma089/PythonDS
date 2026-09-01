device_status = input("Tell me your device status ").lower()
temperature = int(input("Tell me about Temperature "))


if device_status=='active':
    if temperature>35:
        print("High Temperature alert")
    else:
        print("Temperature Normal")
else:
    print("device is offline")