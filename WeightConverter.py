# rounding-capable weight converter:
while True:
    userInput1 = input("Weight: ")
    if userInput1.lower() == "help":
        print("Type a number as weight. Type 'quit' to exit.")
    elif userInput1.lower() == "quit":
        break
    elif type(float(userInput1)) != float:
        print("Not a valid value for 'Weight'. Type 'help' to display commands.")
    else:
        weight = float(userInput1)
        userInput2 = input("(K)g or (L)bs: ")
        if userInput2 == "help":
            print("Type 'K' to set the Unit of Measurement as Kg and convert to Lbs;\nType 'L' to set the Unit of measurement as Lbs and convert to Kg.\nType 'quit' to exit.")
        elif userInput2 == "quit":
            break
        else:
            unitOfMeasurement = userInput2.upper()
            if unitOfMeasurement == "K":
                print("Weight in Lbs: " + str(float(weight / 0.45).__round__(2)))
            elif unitOfMeasurement == "L":
                print("Weight in Kgs: " + str(float(weight * 0.45).__round__(2)))
            else:
                print("Not a valid unit of measurement")
print("Done")