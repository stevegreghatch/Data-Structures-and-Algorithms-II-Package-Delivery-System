from Distance import *
from Truck import *
from Package import *

# Initialization  ------------------------------------------------------------------------------------------------------
# O(1) constant
rate = 18  # miles per hour

# list of times between locations
# O(1) constant
timeBetweenLocationsListT1 = []
timeBetweenLocationsListT2 = []
timeBetweenLocationsListT3 = []

# list of delivery times - returned to setDeliveryTimeStamp
# O(1) constant
deliveryTimesToReturnT1 = []
deliveryTimesToReturnT2 = []
deliveryTimesToReturnT3 = []

# Time Functions -------------------------------------------------------------------------------------------------------
# populate list of time between locations
# 0(N) linear
def setTimeBetweenLocationsListT1():
    # list cleared to allow for multiple function calls
    timeBetweenLocationsListT1.clear()
    for distance in distanceFloatListT1:
        timeBetweenLocationT1 = (distance / rate) * 60
        timeBetweenLocationsListT1.append(round(timeBetweenLocationT1))
    # print(timeBetweenLocationsListT1)
# 0(N) linear
def setTimeBetweenLocationsListT2():
    # list cleared to allow for multiple function calls
    timeBetweenLocationsListT2.clear()
    for distance in distanceFloatListT2:
        timeBetweenLocationT2 = (distance / rate) * 60
        timeBetweenLocationsListT2.append(round(timeBetweenLocationT2))
    # print(timeBetweenLocationsListT2)
# 0(N) linear
def setTimeBetweenLocationsListT3():
    # list cleared to allow for multiple function calls
    timeBetweenLocationsListT3.clear()
    for distance in distanceFloatListT3:
        timeBetweenLocationT3 = (distance / rate) * 60
        timeBetweenLocationsListT3.append(round(timeBetweenLocationT3))
    # print(timeBetweenLocationsListT3)
# combines above functions
# 0(N) linear
def setTimeBetweenLocationsListAllTrucks():
    setTimeBetweenLocationsListT1()
    setTimeBetweenLocationsListT2()
    setTimeBetweenLocationsListT3()

# set/return time of delivery time for each package - passed into setDeliveryTimeStamp
# O(N) linear
def setAndReturnDeliveryTimesT1():
    # list cleared to allow for multiple function calls
    deliveryTimesToReturnT1.clear()
    previousSetTime = getTimeLeftHub('T1')
    # [:-1] used to drop last time (last time = time from last location to hub)
    for i in timeBetweenLocationsListT1[:-1]:
        timeToSet = (int(previousSetTime) + i)
        # print(timeToSet)
        # convert to string to apply proper formatting
        stringTime = str(timeToSet)
        newFormattedTime = stringTime
        # convert to real time ex. 0866 to 0906
        if stringTime[-2:] >= '60':
            revertedIntTime = int(stringTime)
            newIntTime = revertedIntTime + 40
            stringTime = str(newIntTime)
            newFormattedTime = stringTime
        if len(stringTime) == 3:
            newFormattedTime = '0' + stringTime
        deliveryTimesToReturnT1.append(newFormattedTime)
        previousSetTime = newFormattedTime
    # print(deliveryTimesToReturnT1)
    return deliveryTimesToReturnT1
# O(N) linear
def setAndReturnDeliveryTimesT2():
    # list cleared to allow for multiple function calls
    deliveryTimesToReturnT2.clear()
    previousSetTime = getTimeLeftHub('T2')
    # [:-1] used to drop last time (last time = time from last location to hub)
    for i in timeBetweenLocationsListT2[:-1]:
        timeToSet = (int(previousSetTime) + i)
        # print(timeToSet)
        # convert to string to apply proper formatting
        stringTime = str(timeToSet)
        newFormattedTime = stringTime
        # convert to real time ex. 0866 to 0906
        if stringTime[-2:] >= '60':
            revertedIntTime = int(stringTime)
            newIntTime = revertedIntTime + 40
            stringTime = str(newIntTime)
            newFormattedTime = stringTime
        if len(stringTime) == 3:
            newFormattedTime = '0' + stringTime
        deliveryTimesToReturnT2.append(newFormattedTime)
        previousSetTime = newFormattedTime
    # print(deliveryTimesToReturnT2)
    return deliveryTimesToReturnT2
# O(N) linear
def setAndReturnDeliveryTimesT3():
    # list cleared to allow for multiple function calls
    deliveryTimesToReturnT3.clear()
    previousSetTime = getTimeLeftHub('T3')
    # [:-1] used to drop last time (last time = time from last location to hub)
    for i in timeBetweenLocationsListT3[:-1]:
        timeToSet = (int(previousSetTime) + i)
        # print(timeToSet)
        # convert to string to apply proper formatting
        stringTime = str(timeToSet)
        newFormattedTime = stringTime
        # convert to real time ex. 0866 to 0906
        if stringTime[-2:] >= '60':
            revertedIntTime = int(stringTime)
            newIntTime = revertedIntTime + 40
            stringTime = str(newIntTime)
            newFormattedTime = stringTime
        if len(stringTime) == 3:
            newFormattedTime = '0' + stringTime
        deliveryTimesToReturnT3.append(newFormattedTime)
        previousSetTime = newFormattedTime
    # print(deliveryTimesToReturnT3)
    return deliveryTimesToReturnT3

# set delivery timestamp as package status
# 0(N^2) quadratic
def setDeliveryTimeStampT1():
    deliveryTimesT1 = setAndReturnDeliveryTimesT1()
    for indexOfDeliveryTime, deliveryTime in enumerate(deliveryTimesT1):
        timestamp = deliveryTime
        formattedTimestamp = timestamp[0] + timestamp[1] + ':' + timestamp[2] + timestamp[3]
        for i in range(len(packageHashTable.table)):
            p = (packageHashTable.search(i + 1))
            pID = int((getattr(p, 'ID')))
            if pID == packageListT1[indexOfDeliveryTime]:
                setattr(p, 'status', ('Delivered at ' + formattedTimestamp))
                packageHashTable.insert(pID, p)
# 0(N^2) quadratic
def setDeliveryTimeStampT2():
    deliveryTimesT2 = setAndReturnDeliveryTimesT2()
    for indexOfDeliveryTime, deliveryTime in enumerate(deliveryTimesT2):
        timestamp = deliveryTime
        formattedTimestamp = timestamp[0] + timestamp[1] + ':' + timestamp[2] + timestamp[3]
        for i in range(len(packageHashTable.table)):
            p = (packageHashTable.search(i + 1))
            pID = int((getattr(p, 'ID')))
            if pID == packageListT2[indexOfDeliveryTime]:
                setattr(p, 'status', ('Delivered at ' + formattedTimestamp))
                packageHashTable.insert(pID, p)
# 0(N^2) quadratic
def setDeliveryTimeStampT3():
    deliveryTimesT3 = setAndReturnDeliveryTimesT3()
    for indexOfDeliveryTime, deliveryTime in enumerate(deliveryTimesT3):
        timestamp = deliveryTime
        formattedTimestamp = timestamp[0] + timestamp[1] + ':' + timestamp[2] + timestamp[3]
        for i in range(len(packageHashTable.table)):
            p = (packageHashTable.search(i + 1))
            pID = int((getattr(p, 'ID')))
            if pID == packageListT3[indexOfDeliveryTime]:
                setattr(p, 'status', ('Delivered at ' + formattedTimestamp))
                packageHashTable.insert(pID, p)
# combines above functions
# 0(N^2) quadratic
def setDeliveryTimeStampAllTrucks():
    setDeliveryTimeStampT1()
    setDeliveryTimeStampT2()
    setDeliveryTimeStampT3()
