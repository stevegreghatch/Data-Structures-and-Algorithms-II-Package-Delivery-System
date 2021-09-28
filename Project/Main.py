# Steven Hatch - Student ID: -

# B3: Space-time Complexity:
    # each major segment of program included in line
    # entire program = O(N^2) quadratic

from Time import *
from Self_Adjusting_Algorithms import *

# Initialization -------------------------------------------------------------------------------------------------------
# set package data
setPackageData('WGUPS Package File.csv')                                               # O(N) linear

# Main Functions -------------------------------------------------------------------------------------------------------

# init function
# O(N^2) quadratic
def mainUserInterfaceInit():
    # set packages in trucks - prioritizes delivery deadlines and follows project requirements
    setPackagesInTrucks()  # set packageList                                           # O(N^2) quadratic

    # set distance data
    setPackageListAddressesAllTrucks()  # set street addresses list                    # O(N^2) quadratic
    setAddressKeyListAllTrucks()  # set address keys/names list                        # O(N^2) quadratic
    setUniqueAddressKeyListAllTrucks()  # set unique address keys/names                # O(N) linear
    setAllAddressesInOptimalRouteOrderAllTrucks()  # set optimal address keys/names    # O(N^2) quadratic
    setOptimalPackageListAddressesAllTrucks()  # set optimal street addresses list     # O(N^2) quadratic
    setOptimalPackageListAllTrucks()  # set optimal package list                       # O(N^2) quadratic
    setTotalRouteMileageAllTrucks()  # set total route mileage                         # O(N^2) quadratic

    # set time data
    setTimeBetweenLocationsListAllTrucks()  # set time between locations               # 0(N) linear
    setDeliveryTimeStampAllTrucks()  # set delivery timestamp as package status        # 0(N^2) quadratic

# updates package delivery address based on specified criteria then re-initializes data
# ex. update package 9's delivery address if time is past 1020 to meet project requirement
# O(N^2) quadratic -- due to mainUserInterfaceInit() call
def deliveryAddressUpdateCheck(userInputTime):
    for i in range(len(packageHashTable.table)):
        p = (packageHashTable.search(i + 1))
        pID = int((getattr(p, 'ID')))
        if pID == 9 and userInputTime > '1020':
            # update to correct address
            setattr(p, 'address', '410 S State St')
    mainUserInterfaceInit()

# User Interface
# O(N^2) quadratic

# validates entered time before moving to main form
# O(1) constant
def mainUserInterface():
    print('\nEnter a time after 08:00:00 (in military time, i.e., 0900)')
    userInputTime = input()
    # time formatting check
    if len(userInputTime) != 4:
        print('Time must be 4 digits')
        mainUserInterface()
    if userInputTime >= '2400' or '-' in userInputTime:
        print('Time must be between 0000 and 2359')
        mainUserInterface()

    # user interface main form
    # O(N^2) quadratic
    def mainForm():
        print('\nEnter an Option:')
        print('1: View All Data (all trucks + all packages)')
        print('2: View Truck Data')
        print('3: View Package Data')
        userInput = input()
        if userInput == '1':
            deliveryAddressUpdateCheck(userInputTime)                # O(N^2) quadratic
            getAllDataAtSetTime(userInputTime)                       # O(N) linear
            mainFormQuit()                                           # O(1) constant
        elif userInput == '2':
            deliveryAddressUpdateCheck(userInputTime)                # O(N^2) quadratic
            getAllTruckDataAtSetTime(userInputTime)                  # O(N) linear
            mainFormQuit()                                           # O(1) constant
        elif userInput == '3':
            # O(N^2) quadratic
            def packageSearch():
                print('\nEnter an Option:')
                print('1: View All Package Data')
                print('2: View Specific Package Data by ID')
                userInputPackageSearch = int(input())
                if userInputPackageSearch == 1:
                    deliveryAddressUpdateCheck(userInputTime)         # O(N^2) quadratic
                    getAllPackageDataAtSetTime(userInputTime)         # O(N) linear
                    mainFormQuit()                                    # O(1) constant
                elif userInputPackageSearch == 2:
                    deliveryAddressUpdateCheck(userInputTime)         # O(N^2) quadratic
                    getSpecificPackageDataAtSetTime(userInputTime)    # O(N) linear
                    mainFormQuit()                                    # O(1) constant
                else:
                    print('Please enter a number 1-2')
                    packageSearch()                                   # O(N^2) quadratic
            packageSearch()                                           # O(N^2) quadratic
        else:
            print('Please enter a number 1-3')
            mainForm()                                                # O(N^2) quadratic
    mainForm()                                                        # O(N^2) quadratic

# quits program
# O(1) constant
def mainFormQuit():
    print('\nRun again for new search')
    quit()

# Main Function Calls --------------------------------------------------------------------------------------------------

mainUserInterfaceInit()                                                # O(N^2) quadratic
mainUserInterface()                                                    # O(N^2) quadratic
