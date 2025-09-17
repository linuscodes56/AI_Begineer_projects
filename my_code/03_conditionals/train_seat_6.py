seat_type = input("Select from seat type: sleeper, AC, general, luxuary.\n").lower()

match seat_type:
    case "sleeper":
        print("1")
    
    case "ac":
        print("2")
    
    case "genearl":
        print("3")
    
    case "luxuary":
        print("4")
    
    case _:
        print("Invalid seat type ")
    