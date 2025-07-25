command = ""
while True:
    command = input ("> ")
    if command == "start":
        print ("car started")
    elif command == "stop":
        print ("car stoped")
    elif command == "help":
        print ('''
start ==========> car started
stop  ==========> car stoped
quit  ==========> quit
''')