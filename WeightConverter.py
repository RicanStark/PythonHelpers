# rounding-capable weight converter:
weight = float(input("Weight: "))
unitOfMeasurement = input("(K)g or (L)bs: ")
if unitOfMeasurement.upper() == "K":
    print("Weight in Lbs: " + str(float(weight / 0.45).__round__(2)))
elif unitOfMeasurement.upper() == "L":
    print("Weight in Kgs: " + str(float(weight * 0.45).__round__(2)))
else:
    print("Not a valid unit of measurement")
print("Done")

# to do: make the program continue to run after last input; add input option to terminate program