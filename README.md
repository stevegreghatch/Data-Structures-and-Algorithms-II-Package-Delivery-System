# Data Structures and Algorithms II 

SOLUTION

    o  Self-adjusting algorithms
        o  Greedy Algorithm = setPackagesInTrucks()  
        o  Nearest Neighbor Algorithm = setOptimalPackageListAllTrucks()

    o  Overview of Program
    
        o  Self Adjusting Algorighms
            o  Self-Adjusting Algorithm #1 - Greedy Algorithm - setPackagesInTrucks()
                o  Overview: algorithm prioritizes earliest deadline times and fills up first two departing trucks (T1 and T2)
                    o  algorithm gets list of all packages sorted by earliest deadline from getPackageDeliveryDeadlineList()
                    o  algorithm places packages in first two trucks until they are full (# 14 package limit for equal distribution)
                    o  algorithm places remaining packages in truck departing latest (T3)
                    o  while placing packages, algorithm appends each package to packagesAlreadyPlaced list to prevent duplicates in event that algorithm needs to be called again (if deadlines change, if total number of packages change, etc.)
            o  Self-Adjusting Algorithm #2 - Nearest Neighbor Algorithm - setOptimalPackageListAllTrucks()
                o   Overview: algorithm sets optimal package list order to minimize route mileage for each truck
                    o  algorithm searches all possible destinations to determine shortest location from hub, then loops to determine shortest distance from each location to the                         next, then optimally sets address key/names - loopToSetAllAddressesInOptimalRouteOrder() - getShortestDistanceFromHub(), getNextShortestDistanceForRouteList()
                    o  algorithm then converts optimally sorted address key/names into optimally sorted street addresses - setOptimalPackageListAddressesT1()
                    o  algorithm then matches optimally sorted street addresses to package delivery destinations and sets package IDs in optimal order - setOptimalPackageListT1()
                    o  algorithm then replaces packageList with optimalPackageList

        o  Environment
            o  PyCharm on Windows 10 64-bit OS

        o  Space-Time Complexity
            o  Complexity of each major segment of program, and the entire program, using big-0 notation included in code comments

        o  Capability of solution to scale and adapt to a growing number of packages
            o  Hash table includes parameter to change initial capacity, allowing for additional package storage
            o  CSV import is capable of reading and storing additional packages from larger package lists
            o  Self-adjusting algorithm #1: packages are self-placed into trucks based on delivery deadline and truck departure time
            o  Self-adjusting algorithm #2: packages are self-sorted to determine optimal delivery route (lowest mileage)
            o  Main function deliveryAddressUpdateCheck: updates package delivery address based on specified criteria then re-initializes data
            o  Identified constraints are number of trucks, overall truck package capacity, and number of truck drivers

        o  Discussion of why the software is efficient and easy to maintain
            o  Efficiency 
                o  Big-O time complexity of entire program = O(N^2) quadratic
                o  User Interface
                    o  Straightforward prompts for user to get desired data
            o  Maintainability for Future Developers
                o  Code structure 
                    o  Each py file follows same formation (ex. initialization, functions)
                o  Code comments
                    o  Each major section of code is labeled with its purpose
                o  Compartmentalization
                    o  All major functions have been combined for easier readability (ex. setTotalRouteMileageAllTrucks instead of setForT1, setForT2, setForT3 
                    o  Main file only requires two function calls
                        o  mainUserInterfaceInit()
                        o  mainUserInterface()

        o  Strengths and weaknesses of the self-adjusting data structures
            o  Hash Table
                o  Strengths
                    o  Allows for fast inserts, searches, and removals (up to O(1))
                    o  Easy to implement (python has built-in hash() function)
                    o  Excellent for data integrity verification and cryptography
                o  Weaknesses
                    o  Needs to be designed to avoid collisions
                    o  Slow if there are a high number of collisions
                    o  Helps to know all possible item keys beforehand (not always available)

    o  Original program written to deliver all packages, meeting all requirements, using the attached supporting documents
                o  Comments in code have been included to explain process and flow of program.

    o  Self-adjusting data structure that can be used with self-adjusting algorithms to store the package data
        o  hash table

        o  Explanation of how data structure accounts for the relationship between the data points being stored
            o  Relationship between data points being stored and hash table
                o  Data points being stored = package data
                o  Package data is stored in hash table as package objects
                    o  p = Package( pID, pAddress, pCity, pState, pZipCode, pDeadline, pWeight, pSpecialNotes, pStatus)
                    o  Inserted into hash table as packageHashTable.insert(pID, p)
                        o  pID = key to search, insert(update/insert new), and remove package object from hash table
            o  Hash table retrieves information accurately and more efficiently than linear search due to its bucket design
                o  Bucket is determined by hash(key) % len(self.table)
                    o  ex. package 40
                        o  Instead of searching 1-40 to find p40 (linear search) (O(N)), hash table allows for p40 to be placed in bucket 0 and found at O(1)
            o  Relationship between self-adjusting algorithm #1 (greedy algorithm) and hash table
                o  Algorithm searches through all package objects in hash table to build package list sorted by pDeadline (delivery deadlines)
                    o  This list (sortedDeadlineList) is then implemented to set packages with earlier delivery deadlines to the trucks departing earliest
            o  Relationship between self-adjusting algorithm #2 (nearest neighbor) and hash table
                o  After determining optimal routes for all trucks, algorithm searches through package objects in hash table to verify that a match has been found between addresses                 in optimalPackageListAddresses (optimal street addresses) and pAddresses (addresses of packages from hash table)
                    o  Once match is found, pID (package ID) is appended to optimalPackageList

    o  Hash table developed without using any additional libraries or classes. Hash table has an insertion function that takes all required components as input and inserts all required components in the hash table 
        o  see Hash.py, Hash.py – insert, Package.py - packageHashTable.insert(pID, p)

    o  Look-up function developed that uses package IDs as input and returns all corresponding package data elements 
        o  see Hash.py – search, Package.py – getPackageDataByID

    o  User interface provided that allows viewing of status and info of any package at any time, and the total mileage traveled by all trucks
        o  see Main.py – mainUserInterface
        o  all screenshots are included in zip file submission in project_screenshots folder
            o  screenshot of the status of all packages at a time between 8:35am and 9:25am (time=8:45am)
            o  screenshot of the status of all packages at a time between 9:35am and 10:25am (time=10:15am)
            o  screenshot of the status of all packages at a time between 12:03pm and 1:12pm (time=1:05pm/13:05 military time) 

    o  Screenshot provided showing successful completion of the code, free from runtime errors or warnings, that includes total mileage traveled by all trucks
        o  screenshot included in zip file submission in project_screenshots folder

    o  Justification of core algorithms

        o  Strengths of the algorithms used
            o  Self-Adjusting Algorithm #1 - Greedy Algorithm - setPackagesInTrucks()
                o  Ensures that packages with earliest delivery times are placed on first departing trucks
                    o  Aims to prevent delivery past delivery deadline
                        o  Works for this project (unsure about scalability)
                o  Prevents duplicate packages being added to trucks (in event that algorithm needs to be called again (if deadlines change, if total number of packages                 change, etc.)
                    o  see Self_Adjusting_Algorithms.py, packagesAlreadyPlaced
            o  Self-Adjusting Algorithm #2 - Nearest Neighbor Algorithm - setOptimalPackageListAllTrucks()
                o  Sets optimal package list order to minimize route mileage for each truck
                o  Allows flexibility of package list size
                    o  Based on number of packages in truck == number of unique address + duplicate address
                    o  see Distance.py, loopToSetAllAddressesInOptimalRouteOrder
                o  Accounts for duplicate delivery addresses
                    o  Appends duplicate delivery address after first instance of address to maintain optimal route / package list order
                    o  see Distance.py, loopToSetAllAddressesInOptimalRouteOrder

        o  Verification that the algorithm used meets all requirements:
            o  Total combined miles traveled by all trucks = 130.7 miles
                o  Can verify through user interface, ‘View Truck Data’
                o  Can also verify by enabling the following print functions:
                    o  Diatance.py (original print not reflective of optimal miles – check console after entering time into user interface to see print of total miles that were set based on optimal route being calculated ex. T2 miles = 58.1 -> 52.8)
                        o  setTotalRouteMileageAllTrucks(), print(mileageToSetT1)
                        o  setTotalRouteMileageAllTrucks(), print(mileageToSetT2)
                        o  setTotalRouteMileageAllTrucks(), print(mileageToSetT3)

            o  All packages were delivered on time
                o  Can verify through user interface, enter time >= 1159
                o  Can also verify by enabling the following print functions:
                o  Distance.py (float list of route distance ---- last distance = distance to hub)
                    o  updateTotalMilesAndPopulateDistancesT1(), print(distanceFloatListT1)
                    o  updateTotalMilesAndPopulateDistancesT2(), print(distanceFloatListT2)
                    o  updateTotalMilesAndPopulateDistancesT3(), print(distanceFloatListT3)
                o  Time.py (time between locations in minutes ---- last time = distance to hub)
                    o  setTimeBetweenLocationsListT1 (), print(timeBetweenLocationsListT1)
                    o  setTimeBetweenLocationsListT2 (), print(timeBetweenLocationsListT2)
                    o  setTimeBetweenLocationsListT3 (), print(timeBetweenLocationsListT3)
                o  Time.py (delivery times -- original print not reflective of optimal times – check console after entering time into user interface to see print of delivery times that were set based on optimal route being calculated ex. deliveryTimesToReturnT2 last delivery = 1051 ->  1033)
                    o  setAndReturnDeliveryTimesT1(), print(deliveryTimesToReturnT1)
                    o  setAndReturnDeliveryTimesT2(), print(deliveryTimesToReturnT2)
                    o  setAndReturnDeliveryTimesT3(), print(deliveryTimesToReturnT3)

            o  All packages were delivered according to their delivery specifications
                o  Packages 13, 14, 15, 16, 19, and 20 initialized in truck 1
                    o  Meets requirement of being out for delivery on same truck
                    o  To verify, see Self_Adjusting_Algorithms.py, packageListT1
                    o  Can also verify package list by enabling the following print function:
                        o  Distance.py
                            o  setOptimalPackageListAllTrucks, print(optimalPackageListT1)
                o  Packages 3, 18, 36, and 38 initialized in truck 2
                    o  Meets requirement of only being delivered by truck 2
                    o  To verify, see Self_Adjusting_Algorithms.py, packageListT2
                    o  Can also verify package list by enabling the following print function:
                        o  Distance.py
                        o  setOptimalPackageListAllTrucks, print(optimalPackageListT2)
                o  Packages 6, 25, 28, and 32 initialized in truck 3
                    o  Meets requirement of not leaving hub until 9:05am
                    o  To verify, see Self_Adjusting_Algorithms.py, packageListT3 and Truck.py, timeLeftHubT3
                    o  Can also verify package list by enabling the following print function:
                        o  Distance.py
                            o  setOptimalPackageListAllTrucks, print(optimalPackageListT3)
                o  Package 9 also initialized in truck 3
                    o  Meets requirement of not being delivered until 10:20am
                    o  To verify, see package 9 delivery time through UI console output
                        o  Package 9 is delivered at 10:33am

        o  Two other named algorithms, different from the algorithms implemented, that would meet the requirements in the scenario
            o  Dijkstra’s Shortest Path Algorithm
                o  Could be implemented to minimize total mileage
            o  Breadth-first search
                o  Could also be implemented to minimize total mileage
            o  How both algorithms differ from my algorithm
                o  My solution is not graph based
                o  My solution only finds the shortest path from one location to the next (irrespective of each location’s distance from starting location / hub)
                o  Dijkstra’s Shortest Path Algorithm
                    o  Dijkstra’s algorithm “finds the shortest path from a start vertex to each vertex in a graph”
                o  Breadth-first search
                    o  Breadth-first search “visits a starting vertex, then all vertices of distance 1 from that vertex, then of distance 2, and so on, without                                         revisiting a vertex.”

    o  If I was to do this project again, other than attempting to implement the algorithms previously mentioned, I would do the following
        o  Implement randomization of packages into the truck loading
            o  This could allow for more optimal routes as the result of the lowest total mileage through randomization could be logged, then saved, to place the packages in that specific order, thus decreasing total mileage
        o  Redistribute my functions
            o  Most of them ended up being more conveniently placed in the Distance.py file (leaving the other files sparser)

    o  Justification of the data structure (hash table)

        o  Verification that the data structure used meets all requirements in the scenario
            o  Total combined miles traveled by all trucks = 130.7 miles
            o  All packages were delivered on time
            o  All packages were delivered according to their delivery specifications
            o  An ‘efficient’ hash table with a look-up function is present
            o  The ‘reporting’ (package statuses and information) can be verified through the user interface
                o  All information is accurate

            o  Time needed to complete the look-up function is affected by changes in the number of packages to be delivered
                o  If additional packages need to be delivered, additional packages will need to be added, resulting in inevitable collisions, thus resulting in longer look-up                     times unless structural change is made to the hash table (i.e., adding more buckets)

            o  The data structure space usage is affected by changes in the number of packages to be delivered 
                o  If additional packages are added, buckets in the hash table will become fuller, prompting a need for a solution on how to deal with collisions (potentially needing more space)
                o  If packages are removed, buckets in the hash table will become emptier, freeing space usage for packages being added in the future to utilize

            o  Changes to the number of trucks or the number of cities would affect the look-up time and the space usage of the structure
                o  As the hash table is only implemented to store package data, changes specific to the number of trucks or the number of cities would not directly affect the look-up time or the space usage of the data structure
                o  However, alongside the assumption that more packages would need to be delivered (based on in increase in the number of trucks and delivery to more cities), the look-up function would become slower due to collisions as more packages would need to be added to the table
                o  Look-up speed could be increased at the cost of additional space usage (more buckets would need to be added)

    o  Two other data structures that could meet the same requirements in the scenario
        o  Data structure 1 = Dictionary / Nested Dictionary 
            o  Rather than storing packages as objects in the hash table, packages could be stored as key/value(s) pair in a dictionary
            o  This would allow for convenience of dictionary method usage (ex. update, pop, for key in dictionary loop)
            o  This would add consistency in the project as the distance data is implemented as a dictionary
        o  Data structure 2 = Set with BST 
            o  Contrasting with the hash table, a set would allow for operations such as union, intersection, and difference when comparing two sets, filter to create a subset, and map to create a new set based on a function
            o  Packages could be established as a dynamic set or static set


--------------------------------------------------------------------------------

SCENARIO

The Western Governors University Parcel Service (WGUPS) needs to determine an efficient route and delivery distribution for their Daily Local Deliveries (DLD) because packages are not currently being consistently delivered by their promised deadline. The Salt Lake City DLD route has three trucks, two drivers, and an average of 40 packages to deliver each day. Each package has specific criteria and delivery requirements.

Your task is to determine an algorithm, write code, and present a solution where all 40 packages (listed in the attached “WGUPS Package File”) will be delivered on time while meeting each package’s requirements and keeping the combined total distance traveled under 140 miles for both trucks. The specific delivery locations are shown on the attached “Salt Lake City Downtown Map,” and distances to each location are given in the attached “WGUPS Distance Table.” The intent is to use the program for this specific location and also for many other cities in each state where WGU has a presence. As such, you will need to include detailed comments to make your code easy to follow and to justify the decisions you made while writing your scripts.

Keep in mind that the supervisor should be able to see, at assigned points, the progress of each truck and its packages by any of the variables listed in the “WGUPS Package File,” including what has been delivered and at what time the delivery occurred.

ASSUMPTIONS
*  Each truck can carry a maximum of 16 packages, and the ID number of each package is unique.
*  The trucks travel at an average speed of 18 miles per hour and have an infinite amount of gas with no need to stop.
*  There are no collisions.
*  Three trucks and two drivers are available for deliveries. Each driver stays with the same truck as long as that truck is in service.
*  Drivers leave the hub no earlier than 8:00 a.m., with the truck loaded, and can return to the hub for packages if needed. 
*  The delivery and loading times are instantaneous, i.e., no time passes while at a delivery or when moving packages to a truck at the hub (that time is factored into the calculation of the average speed of the trucks).
*  There is up to one special note associated with a package.
*  The delivery address for package #9, Third District Juvenile Court, is wrong and will be corrected at 10:20 a.m. WGUPS is aware that the address is incorrect and will be updated at 10:20 a.m. However, WGUPS does not know the correct address (410 S State St., Salt Lake City, UT 84111) until 10:20 a.m.
*  The distances provided in the WGUPS Distance Table are equal regardless of the direction traveled.
*  The day ends when all 40 packages have been delivered.

REQUIREMENTS

    A.  Identify a named self-adjusting algorithm (e.g., “Nearest Neighbor algorithm,” “Greedy algorithm”) that you used to create your program to deliver the packages.
    
    B.  Write an overview of your program, in which you do the following:
            1.  Explain the algorithm’s logic using pseudocode.
            2.  Describe the programming environment you used to create the Python application.
            3.  Evaluate the space-time complexity of each major segment of the program, and the entire program, using big-O notation.
            4.  Explain the capability of your solution to scale and adapt to a growing number of packages.
            5.  Discuss why the software is efficient and easy to maintain.
            6.  Discuss the strengths and weaknesses of the self-adjusting data structures (e.g., the hash table).
        
    C.  Write an original program to deliver all the packages, meeting all requirements, using the attached supporting documents “Salt Lake City Downtown Map,” “WGUPS Distance Table,” and the “WGUPS Package File.”
            1.  Create an identifying comment within the first line of a file named “main.py” that includes your first name, last name, and student ID.
            2.  Include comments in your code to explain the process and the flow of the program.
        
    D.  Identify a self-adjusting data structure, such as a hash table, that can be used with the algorithm identified in part A to store the package data.
            1.  Explain how your data structure accounts for the relationship between the data points you are storing. _Note: Use only appropriate built-in data structures, except dictionaries. You must design, write, implement, and debug all code that you turn in for this assessment. Code downloaded from the Internet or acquired from another student or any other source may not be submitted and will result in automatic failure of this assessment._
        
    E.  Develop a hash table, without using any additional libraries or classes, that has an insertion function that takes the following components as input and inserts the components into the hash table:
            1.  Package ID number
            2.  Delivery address
            3.  Delivery deadline
            4.  Delivery city
            5.  Delivery zip code
            6.  Package weight
            7.  Delivery status (e.g., delivered, en route)
        
    F.  Develop a look-up function that takes the following components as input and returns the corresponding data elements:
            1.  Package ID number
            2.  Delivery address
            3.  Delivery deadline
            4.  Delivery city
            5.  Delivery zip code
            6.  Package weight
            7.  Delivery status (i.e., “at the hub,” “en route,” or “delivered”), including the delivery time
        
    G.  Provide an interface for the user to view the status and info (as listed in part F) of any package at any time, and the total mileage traveled by all trucks. (The delivery status should report the package as at the hub, en route, or delivered. Delivery status must include the time.)
            1.  Provide screenshots to show the status of all packages at a time between 8:35 a.m. and 9:25 a.m.
            2.  Provide screenshots to show the status of all packages at a time between 9:35 a.m. and 10:25 a.m.
            3.  Provide screenshots to show the status of all packages at a time between 12:03 p.m. and 1:12 p.m.
        
    H.  Provide a screenshot or screenshots showing successful completion of the code, free from runtime errors or warnings, that includes the total mileage traveled by all trucks.
    
    I.  Justify the core algorithm you identified in part A and used in the solution by doing the following:
            1.  Describe at least two strengths of the algorithm used in the solution.
            2.  Verify that the algorithm used in the solution meets all requirements in the scenario.
            3.  Identify two other named algorithms, different from the algorithm implemented in the solution, that would meet the requirements in the scenario.
                    a.  Describe how each algorithm identified in part I3 is different from the algorithm used in the solution.
            
    J.  Describe what you would do differently, other than the two algorithms identified in I3, if you did this project again.
    
    K.  Justify the data structure you identified in part D by doing the following:
            1.  Verify that the data structure used in the solution meets all requirements in the scenario. Explain how the time needed to complete the look-up function is affected by changes in the number of packages to be delivered. Explain how the data structure space usage is affected by changes in the number of packages to be delivered. Describe how changes to the number of trucks or the number of cities would affect the look-up time and the space usage of the data structure.
            2.  Identify two other data structures that could meet the same requirements in the scenario. Describe how each data structure identified in part K2 is different from the data structure used in the solution.

    L.  Acknowledge sources, using in-text citations and references, for content that is quoted, paraphrased, or summarized.
