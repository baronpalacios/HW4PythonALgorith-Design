def optimalStops(hotelMiles):
    hotelSize = len(hotelMiles)
    penalty = []
    stop = []

    for k in range(0, hotelSize):
        penalty.append(0)
        stop.append(0)

    for i in range(0, hotelSize):
        penalty[i] = pow((200 - hotelMiles[i]), 2)
        for j in range(0, i):
            tempPenalty = penalty[j] + pow((200 - (hotelMiles[i] - hotelMiles[j])), 2)
            if (tempPenalty < penalty[i]):
                penalty[i] = tempPenalty
                stop[i] = j + 1

    print("Minimal Penalty: ", penalty[hotelSize - 1])
    finalPath = ""
    index = len(stop) - 1
    while index >= 0:
        finalPath = str((index + 1)) + " " + finalPath
        index = stop[index] - 1

    print("Optimal Sequence of hotel stop: ", finalPath)


A = [200, 220, 410, 580, 640, 770, 950, 1100, 1350]
optimalStops(A)