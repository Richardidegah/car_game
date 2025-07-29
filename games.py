command = ""
started = False
while command != "quit":
    command = input("> ")
    if command == "on":
        if started:
            print("engine running already")
        else:
            started = True
            print("car engine on")
    elif command == "off":
        if not started:
            print("car engine is power off")
        else:
            started = False
            print("car engine off")

'''command = ""
started = False
while command != "quit":
    command = input("> ").lower()
    if command == "on":
        if started:
            print("car is already on")
        else:
            started = True
            print("car engine on")
    elif command == "off":
        if not started:
            print("car engine off")
    else:
        started = False
        print("car engine is on")
'''