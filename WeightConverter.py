# rounding-capable weight converter:
while True:
    userInput1 = input("Weight: ")
    if userInput1.lower() == "help":
        print("Enter a number as weight. Type 'quit' to exit.")
        continue
    elif userInput1.lower() == "quit":
        break
    try:
        weight = float(userInput1)
    except ValueError:
        print("Not a valid value for 'Weight'. Type 'help' to display commands.")
        continue

    while True:
        userInput2 = input("(K)g or (L)bs: ")
        if userInput2.lower() == "help":
            print("Type 'K' to set the Unit of Measurement as Kg and convert to Lbs;\nType 'L' to set the Unit of measurement as Lbs and convert to Kg.\nType 'quit' to exit.")
            continue
        elif userInput2.lower() == "quit":
            break
        else:
            unitOfMeasurement = userInput2.upper()
            if unitOfMeasurement == "K":
                print("Weight in Lbs: " + str(float(weight / 0.45).__round__(2)))
                break
            elif unitOfMeasurement == "L":
                print("Weight in Kgs: " + str(float(weight * 0.45).__round__(2)))
                break
            else:
                print("Not a valid unit of measurement. Type 'help' to display commands.")
    if userInput2.lower() == "quit":
        break
print("Done")
