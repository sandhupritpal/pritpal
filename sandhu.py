print("""\tThis is a car game 
                                LETS GET STATED  """)
print("\n If you dont know how to play just write help\n \t Thanks.")
started = False
while True :
    command = input(">")
    if command== "quit":
        print("Thanks for playing")
        break
    if command == "start":
        if started :
            print("car already started..")
        else :
            started = True
            print("car started.. ")
    elif command== "stop":
       if not started :
           print("car already stops...")
       else :
           started= False
           print("car stop..")
    elif command== "help":
        print("""write 
        start - to start car 
        stop - to stop car 
        quit - to exit game 
        """)
    else:
        print("invaild ")