from Hash import *
import csv

# Initialization  ------------------------------------------------------------------------------------------------------
# create package hash table
# O(N) linear
packageHashTable = ChainingHashTable(40)

# initialize package class
class Package:
    # O(1) constant
    def __init__(self, ID, address, city, state, zipCode, deadline, weight, specialNotes, status):
        self.ID = ID
        self.address = address
        self.city = city
        self.state = state
        self.zipCode = zipCode
        self.deadline = deadline
        self.weight = weight
        self.specialNotes = specialNotes
        self.status = status

# Package Functions ----------------------------------------------------------------------------------------------------
# set package data to hash table from CSV
# O(N) linear
def setPackageData(fileName):
    with open(fileName) as packageFile:
        packageData = csv.reader(packageFile, delimiter=',')
        next(packageData)  # skip header
        for package in packageData:
            # time conversion
            if package[5] == '9:00 AM':
                package[5] = '0900'
            elif package[5] == '10:30 AM':
                package[5] = '1030'
            elif package[5] == 'EOD':
                package[5] = '1700'
            # assign object attributes
            pID = int(package[0])
            pAddress = package[1]
            pCity = package[2]
            pState = package[3]
            pZipCode = package[4]
            pDeadline = package[5]
            pWeight = package[6]
            pSpecialNotes = package[7]
            pStatus = 'At the Hub'

            # create package object
            p = Package(pID, pAddress, pCity, pState, pZipCode, pDeadline, pWeight, pSpecialNotes, pStatus)

            # set object attributes - insert data into the hash table
            packageHashTable.insert(pID, p)

# formatted search for all package data
# O(N) linear
def getPackageData():
    print('Package Data:')
    for i in range(len(packageHashTable.table)):
        p = (packageHashTable.search(i + 1))
        pID = int((getattr(p, 'ID')))
        pAddress = (getattr(p, 'address'))
        pCity = (getattr(p, 'city'))
        pState = (getattr(p, 'state'))
        pZipCode = (getattr(p, 'zipCode'))
        pDeadline = (getattr(p, 'deadline'))
        pWeight = (getattr(p, 'weight'))
        pSpecialNotes = (getattr(p, 'specialNotes'))
        if pSpecialNotes == '':
            pSpecialNotes = 'n/a'
        pStatus = (getattr(p, 'status'))
        print('Package ID:', pID, '| Address:', pAddress, '| City:', pCity, '| State:', pState, '| Zip:',
              pZipCode, '| Deadline:', pDeadline, '| Weight:', pWeight, '| Special Notes:', pSpecialNotes,
              '| Status:', pStatus)

# formatted search for specific package data by ID
# O(1) constant average
def getPackageDataByID(userInput):
    print('\nRequested Package Data: ')
    p = (packageHashTable.search(userInput))
    pID = int((getattr(p, 'ID')))
    pAddress = (getattr(p, 'address'))
    pCity = (getattr(p, 'city'))
    pState = (getattr(p, 'state'))
    pZipCode = (getattr(p, 'zipCode'))
    pDeadline = (getattr(p, 'deadline'))
    pWeight = (getattr(p, 'weight'))
    pSpecialNotes = (getattr(p, 'specialNotes'))
    if pSpecialNotes == '':
        pSpecialNotes = 'n/a'
    pStatus = (getattr(p, 'status'))
    print('Package ID:', pID, '| Address:', pAddress, '| City:', pCity, '| State:', pState, '| Zip:',
          pZipCode, '| Deadline:', pDeadline, '| Weight:', pWeight, '| Special Notes:', pSpecialNotes,
          '| Status:', pStatus)
