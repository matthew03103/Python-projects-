command = ""
started = False
while True:
    command = input(">").lower()
    if command == "start":
        print('the car has started')
        if started:
            print("the car is already started")
        else:
            started = True
    elif command == 'stop':
        if not started:
            print("the car is already stopped!!")
        else:
            started = False
            print('the car has stopped')
    elif command == 'help':
        print('''
stop - to stop the car
start - to start the car
quit - to quit the game
        ''')
    elif command == "quit":
        break
    else:
        print("I don't understand")