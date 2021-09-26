from Self_Adjusting_Algorithms import *

# Initialization  ------------------------------------------------------------------------------------------------------
# initialize truck class
class Truck:
    # O(1) constant 
    def __init__(self, location, timeLeftHub, totalMileage, totalRouteMileage, packageList, packageNumber):
        self.location = location
        self.timeLeftHub = timeLeftHub
        self.totalMileage = totalMileage
        self.totalRouteMileage = totalRouteMileage
        self.packageList = packageList
        self.packageNumber = packageNumber

# initialize truck values
# O(1) constant
locationT1 = 'At the Hub'
locationT2 = 'At the Hub'
locationT3 = 'At the Hub'
timeLeftHubT1 = '0800'
timeLeftHubT2 = '0800'
timeLeftHubT3 = '1000'  # truck 1 is back at hub at 1000 -- truck 3 returns to hub at 1236
totalMileageT1 = 0
totalMileageT2 = 0
totalMileageT3 = 0
totalRouteMileageT1 = 0
totalRouteMileageT2 = 0
totalRouteMileageT3 = 0

# create truck objects
# O(1) constant
truck1 = Truck(locationT1, timeLeftHubT1, totalMileageT1, totalRouteMileageT1, packageListT1, packageNumberT1)
truck2 = Truck(locationT2, timeLeftHubT2, totalMileageT2, totalRouteMileageT2, packageListT2, packageNumberT2)
truck3 = Truck(locationT3, timeLeftHubT3, totalMileageT3, totalRouteMileageT3, packageListT3, packageNumberT3)

# Truck Functions ------------------------------------------------------------------------------------------------------
# returns time truck left hub
# O(1) constant
def getTimeLeftHub(truckNumber):
    if truckNumber == 'T1':
        return timeLeftHubT1
    elif truckNumber == 'T2':
        return timeLeftHubT2
    elif truckNumber == 'T3':
        return timeLeftHubT3
