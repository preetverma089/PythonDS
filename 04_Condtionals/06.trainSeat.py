seat_type = input("enter your train ticket type ac/sleeper/general/luxury ").lower()

match seat_type:
    case "sleeper":
        print("sleeper me 6 seat")
    case "ac":
        print("ahahaaa thandi hawaaa")
    case "general":
        print("ese garmi marta jaa tu")
    case "luxury":
        print("aghaaa train ka baap bnke ja")
    case _:
        print("seattype not available")