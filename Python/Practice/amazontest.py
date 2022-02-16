def findDataLocations(locations, movedFrom, movedTo):
    # Write your code here
    #We can assume that moved To is and empty array so i can freelly put variables into it
    for x in movedFrom:
        movedTo.append(movedFrom[x] + (movedFrom.index(x) - 1)
    print(movedFrom, movedTo)


tlocations = [1,7,6,8]
tmovedFrom = [1,7,2]
tmovedTo = [2,9,5]
findDataLocations(tlocations,tmovedFrom,tmovedTo)