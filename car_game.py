command = ""
started = True
while command != "quit":
    command = input("> ")
    if command == "on":
        if started:
            print("car engine is already on")
        else:
            started = True
            print("car engine on")
    elif command == "off":
        if not started:
            print ("car engine power is off")
        else:
            started = False
            print ("car engine is off")
    elif command == "help":
        print ("""
stop ===> stop engine
start ===> start engine
help ===> help options
""")