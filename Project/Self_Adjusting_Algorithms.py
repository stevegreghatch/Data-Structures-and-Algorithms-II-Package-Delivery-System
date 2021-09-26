from Package import *
from operator import itemgetter

# Initialization  ------------------------------------------------------------------------------------------------------
# list of packages in each truck
# packages placed based on project requirements (with consideration to optimal mileage)
# O(1) constant
packageListT1 = [13, 14, 15, 16, 19, 20]
packageListT2 = [3, 18, 36, 38]
packageListT3 = [6, 25, 28, 32, 9]

# list of packages already loaded
# O(1) constant
packagesAlreadyPlaced = ['3', '6', '13', '14', '15', '16', '18', '19', '20', '25', '28', '32', '36', '38']

# number of packages in list
# O(1) constant
packageNumberT1 = len(packageListT1)
packageNumberT2 = len(packageListT2)
packageNumberT3 = len(packageListT3)

# list of delivery deadlines to prioritize earlier times
# O(1) constant
deadlineList = []

# Self_Adjusting Algorithms  -------------------------------------------------------------------------------------------

# builds list of delivery deadlines and sorts by earliest time
# O(N log N) log-linear
def getPackageDeliveryDeadlineList():
    # list cleared to allow for multiple function calls
    deadlineList.clear()
    for i in range(len(packageHashTable.table)):
        p = (packageHashTable.search(i + 1))
        pID = str(getattr(p, 'ID'))
        pDeadline = (getattr(p, 'deadline'))
        pListObject = 'Package ID:', pID, 'Deadline:', pDeadline
        deadlineList.append(pListObject)
    sortedDeadlineList = sorted(deadlineList, key=itemgetter(3))
    return sortedDeadlineList

# Self-Adjusting Algorithm #1 - Greedy Algorithm
# setPackagesInTrucks()
# Overview: algorithm prioritizes earliest deadline times and fills up first two departing trucks (T1 and T2)
# 1) algorithm gets list of all packages sorted by earliest deadline from getPackageDeliveryDeadlineList()
# 2) algorithm places packages in first two trucks until they are full (# 14 package limit for equal distribution)
# 3) algorithm places remaining packages in truck departing latest (T3)
# 4) while placing packages, algorithm appends each package to packagesAlreadyPlaced list to prevent duplicates
    # in event that algorithm needs to be called again (if deadlines change, if total number of packages change, etc.)
# O(N^2) quadratic
def setPackagesInTrucks():
    sortedDeadlineList = getPackageDeliveryDeadlineList()
    for package in sortedDeadlineList:
        # package [1] = pID
        if package[1] not in packagesAlreadyPlaced:
            if len(packageListT1) < 14:
                packageListT1.append(int(package[1]))
                packagesAlreadyPlaced.append(package[1])
            elif len(packageListT2) < 14:
                packageListT2.append(int(package[1]))
                packagesAlreadyPlaced.append(package[1])
            else:
                packageListT3.append(int(package[1]))
                packagesAlreadyPlaced.append(package[1])

# Self-Adjusting Algorithm #2 - Nearest Neighbor Algorithm
# setOptimalPackageListAllTrucks() - Found in Distance File at line 425
# Overview: algorithm sets optimal package list order to minimize route mileage for each truck
# 1) algorithm searches all possible destinations to determine shortest location from hub, then loops to determine
# shortest distance from each location to the next, then optimally sets address key/names
    # loopToSetAllAddressesInOptimalRouteOrder()
        # getShortestDistanceFromHub(), getNextShortestDistanceForRouteList()
# 2) algorithm then converts optimally sorted address key/names into optimally sorted street addresses
    # setOptimalPackageListAddressesT1()
# 3) algorithm then matches optimally sorted street addresses to package delivery destinations and sets package IDs
    # in optimal order
        # setOptimalPackageListT1()
# 4) algorithm then replaces packageList with optimalPackageList
# O(N^2) quadratic

    # setOptimalPackageListAllTrucks()
        # gets optimalPackageListT1 from setOptimalPackageListT1()
            # gets optimalPackageListAddressesT1 from setOptimalPackageListAddressesT1()
                # gets optimalAddressKeyListT1 from loopToSetAllAddressesInOptimalRouteOrderT1()
                    # calls getShortestDistanceFromHubT1() and getNextShortestDistanceForRouteListT1()
        # gets optimalPackageListT2 from setOptimalPackageListT2()
            # gets optimalPackageListAddressesT2 from setOptimalPackageListAddressesT2()
                # gets optimalAddressKeyListT2 from loopToSetAllAddressesInOptimalRouteOrderT2()
                    # calls getShortestDistanceFromHubT2() and getNextShortestDistanceForRouteListT2()
        # gets optimalPackageListT3 from setOptimalPackageListT3()
            # gets optimalPackageListAddressesT3 from setOptimalPackageListAddressesT3()
                # gets optimalAddressKeyListT3 from loopToSetAllAddressesInOptimalRouteOrderT3()
                    # calls getShortestDistanceFromHubT3() and getNextShortestDistanceForRouteListT3()
