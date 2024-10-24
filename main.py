#Anthony McUne
#Student ID: 011933865

import sys
import csv
from PackageTable import PackageTable
from PackageClass import Package
from TruckClass import Truck

#Creates package list for use later on
package_list = []
pack_count = 1
while pack_count <= 40:
    package_list.append(pack_count)
    pack_count += 1

#Remove packs manually loaded onto trucks from pack list
special_packs = [22, 8, 4, 11, 23, 13, 14, 15, 16, 19, 20, 21, 1, 6,
                 25, 26, 3, 9, 18, 28, 29, 30, 31, 32, 34, 36, 37, 38, 39, 40]
for pack in special_packs:
    package_list.remove(pack)

def csv_reader(filename):
    '''simple csv reader function
    args:
    filename: str: name of file in current directory or filepath'''
    with open(filename) as fp:
        reader = csv.reader(fp, delimiter=',', quotechar='"')
        package_reader = [row for row in reader]
        fp.close()
        return package_reader

#Reads in package data from csv file and creates package objects
def create_table():
    '''Creates a hashtable from a csv
    file using the PackageTable Class'''
    table = PackageTable()
    package_reader = csv_reader("WGUPS Package File.csv")
    for row in package_reader:
        #Creates package object
        package = Package(row)
        table.insert_package(package.get_packageId(), package)
    return table

def get_distances():
    '''Creates dictionary and reads in addresses and distances from csv'''
    distances = {}
    distance_reader = csv_reader("WGUPS Distance Table.csv")
    for row in distance_reader[1:]:
        i = 0
        for column in row:

            #Exception handling to skip address name rows in iteration
            try:
                float(column)
                if i<28:
                    i += 1
                #Adds distance to dictionary with "address1 to address2" as the key
                distances.update({(str(row[0]) + " to " + str(distance_reader[0][i])): column})
            except ValueError:
                continue
    return distances

def get_addresses():
    '''Creates table of all addresses from csv file'''
    addresses = []
    distance_reader = csv_reader("WGUPS Distance Table.csv")
    for row in distance_reader[1:]:
            addresses.append(row[0])
    return addresses

#Create all table objects
package_table = create_table()
time_pack_table = create_table()
distance_table = get_distances()
addresses = get_addresses()

def find_distance(dist_table:dict, address1:str, address2:str):
    '''Takes two addresses and uses them to create a key to the dict to find the distance
    between the two addresses.
    args:
        dist_table: dict a table created using the get_distances() function
        address1: str an address string from the provided documentation
        address2: str an address string from the provided documentation'''
    #Creates key to table
    distance_key =str(address1 + " to " + address2)
    #Searches table for matching key
    distance = dist_table.get(distance_key)
    #Error block
    if distance != None:
        return float(distance)
    #If error: print error message and exit program
    else:
        print("Error: Invalid Address :" +distance_key)
        sys.exit(1)
        return

def get_packageData_atTime(time, pack_id = 0):
    '''Function to print package data based on a user inputted time
    args: time(in minutes)
    pack_id(pack_id # (1-40))
    '''
    #converts string to int
    time = int(time)
    #Lists for each  manually loaded packs
    truck1_packs = [15, 16, 34, 14, 29, 20, 21, 19, 12, 2, 10, 5, 13, 27, 35, 39]
    truck2_packs = [25, 26, 6, 31, 37, 30, 1, 40, 4, 32, 36, 23, 11, 18, 38, 3]
    truck3_packs = [24, 22, 7, 33, 17, 28, 8]

    #List of all packs
    all_packs = [1, 6, 25, 28, 32, 31, 17, 21, 24, 27, 35, 11, 12, 23, 26, 22, 3, 9, 18, 36, 38, 5, 37, 8, 30, 10, 39, 2, 33, 7, 29, 4, 16, 14, 15, 13, 19, 20, 34, 40]

    #Pack id 0 indicates user wants all package data at a specific time
    if pack_id == 0:
        for pack in all_packs:
            #Determines which truck package was on
            #Obtains delivery time of package from table if the user given time is after
            #the delivery time of the package. If the delivery time is while the truck is enroute
            #(i.e. before package delivery time but after truck departure time), return enroute status.
            #If it is before truck departure time, return in hub status string.
            package_address = str(package_table.find_package_address(pack))  + " " + str(package_table.get_packageCity(pack)) + ", " + str(package_table.get_packageState(pack)) + " " + str(package_table.get_packageZip(pack))
            package_duedate = package_table.get_packageDueDate(pack)
            if pack in truck1_packs:
                if time >= package_table.get_deliv_time(pack):
                    time_tot_min = package_table.get_deliv_time(pack)
                    time_min = str(int(package_table.get_deliv_time(pack))%60)
                    #Formatted time string logic(python datetime was too frustrating)
                    if len(time_min) < 2:
                        del_time = ((str(int(time_tot_min)//60) + ":0" + time_min))
                    else:
                        del_time = ((str(int(time_tot_min)//60) + ":" + time_min))
                    print("Package " + str(pack) + ": " + "Delivered at " + del_time + " by truck1. | Due at: " + str(package_duedate) + " | Address: " + str(package_address))
                elif time >= 480:
                    print("Package " + str(pack) + ": enroute on truck1 | Due at: " + str(package_duedate) + " | Address: " + str(package_address))
                else:
                    print("Package " + str(pack) + ": at hub | Due at: " + str(package_duedate) + " | Address: " + str(package_address))

            if pack in truck3_packs:
                if time >= package_table.get_deliv_time(pack):
                    time_tot_min = package_table.get_deliv_time(pack)
                    time_min = str(int(package_table.get_deliv_time(pack))%60)
                    #Formatted time string logic(python datetime was too frustrating)
                    if len(time_min) < 2:
                        del_time = ((str(int(time_tot_min)//60) + ":0" + time_min))
                    else:
                        del_time = ((str(int(time_tot_min)//60) + ":" + time_min))
                    print("Package " + str(pack) + ": " + "Delivered at " + del_time + " by truck3 | Due at: " + str(package_duedate) + " | Address: " + str(package_address))
                elif time >= 594:
                    print("Package " + str(pack) + ": enroute on truck3 | Due at: " + str(package_duedate) + " | Address: " + str(package_address))
                else:
                    print("Package " + str(pack) + ": at hub | Due at: " + str(package_duedate) + " | Address: " + str(package_address))

            if pack in truck2_packs:
                if time >= package_table.get_deliv_time(pack):
                    time_tot_min = package_table.get_deliv_time(pack)
                    time_min = str(int(package_table.get_deliv_time(pack))%60)
                    #Formatted time string logic(python datetime was too frustrating)
                    if len(time_min) < 2:
                        del_time = ((str(int(time_tot_min)//60) + ":0" + time_min))
                    else:
                        del_time = ((str(int(time_tot_min)//60) + ":" + time_min))
                    print("Package " + str(pack) + ": " + "Delivered at " + del_time + " by truck2 | Due at: " + str(package_duedate) + " | Address: " + str(package_address))
                elif time >= 545:
                    print("Package " + str(pack) + ": enroute on truck2 | Due at: " + str(package_duedate) + " | Address: " + str(package_address))
                else:
                    print("Package " + str(pack) + ": at hub | Due at: " + str(package_duedate) + " | Address: " + str(package_address))

            if pack == 9:
                if time >= 675:
                    time_tot_min = package_table.get_deliv_time(pack)
                    time_min = str(int(package_table.get_deliv_time(pack))%60)
                    #Formatted time string logic(python datetime was too frustrating)
                    if len(time_min) < 2:
                        del_time = ((str(int(time_tot_min)//60) + ":0" + time_min))
                    else:
                        del_time = ((str(int(time_tot_min)//60) + ":" + time_min))
                    print("Package " + str(pack) + ": " + "Delivered at " + del_time + " by truck3 | Due at: " + str(package_duedate) + " | Address: " + str(package_address))
                elif time >= 620:
                    print("Package " + str(pack) + ": enroute on truck3 | Due at: " + str(package_duedate) + " | Address: " + str(package_address))
                elif time >= 594:
                    package_address = "300 State St " + str(package_table.get_packageCity(pack)) + ", " + str(package_table.get_packageState(pack)) + " " + str(package_table.get_packageZip(pack))
                    print("Package " + str(pack) + ": enroute on truck3 | Due at: " + str(package_duedate) + " | Address: " + str(package_address))
                else:
                    package_address = "300 State St " + str(package_table.get_packageCity(pack)) + ", " + str(package_table.get_packageState(pack)) + " " + str(package_table.get_packageZip(pack))
                    print("Package " + str(pack) + ": at hub | Due at: " + str(package_duedate) + " | Address: " + str(package_address))

    #Same idea as above. This time, however, it searches for a single package, using the same logic above, and
    #Returns a single status string.
    if pack_id != 0:
            pack = pack_id
            package_address = str(package_table.find_package_address(pack))  + " " + str(package_table.get_packageCity(pack)) + ", " + str(package_table.get_packageState(pack)) + " " + str(package_table.get_packageZip(pack))

            package_duedate = package_table.get_packageDueDate(pack)
            if pack2: == 9:
                if time >= 675:
                    time_tot_min = package_table.get_deliv_time(pack)
                    time_min = str(int(package_table.get_deliv_time(pack))%60)
                    #Formatted time string logic(python datetime was too frustrating)
                    if len(time_min) < 2:
                        del_time = ((str(int(time_tot_min)//60) + ":0" + time_min))
                    else:
                        del_time = ((str(int(time_tot_min)//60) + ":" + time_min))
                    print("Package " + str(pack) + ": " + "Delivered at " + del_time + " by truck3 | Due at: " + str(package_duedate) + " | Address: " + str(package_address))
                elif time >= 620:
                    print("Package " + str(pack) + ": enroute on truck3 | Due at: " + str(package_duedate) + " | Address: " + str(package_address))
                elif time >= 594:
                    package_address = "300 State St " + str(package_table.get_packageCity(pack)) + ", " + str(package_table.get_packageState(pack)) + " " + str(package_table.get_packageZip(pack))
                    print("Package " + str(pack) + ": enroute on truck3 | Due at: " + str(package_duedate) + " | Address: " + str(package_address))
                else:
                    package_address = "300 State St " + str(package_table.get_packageCity(pack)) + ", " + str(package_table.get_packageState(pack)) + " " + str(package_table.get_packageZip(pack))
                    print("Package " + str(pack) + ": at hub | Due at: " + str(package_duedate) + " | Address: " + str(package_address))

            if pack_id in truck1_packs:
                if time >= package_table.get_deliv_time(pack):
                    time_tot_min = package_table.get_deliv_time(pack)
                    time_min = str(int(package_table.get_deliv_time(pack))%60)
                    #Formatted time string logic(python datetime was too frustrating)
                    if len(time_min) < 2:
                        del_time = ((str(int(time_tot_min)//60) + ":0" + time_min))
                    else:
                        del_time = ((str(int(time_tot_min)//60) + ":" + time_min))
                    print("Package " + str(pack) + ": " + "Delivered at " + del_time + " by truck1 | Due at: " + str(package_duedate) + " | Address: " + str(package_address))
                elif time >= 480:
                    print("Package " + str(pack) + ": enroute on truck1 | Due at: " + str(package_duedate) + " | Address: " + str(package_address))
                else:
                    print("Package " + str(pack) + ": at hub | Due at: " + str(package_duedate) + "  | Address: " + str(package_address))

            if pack_id in truck3_packs:
                if time >= package_table.get_deliv_time(pack):
                    time_tot_min = package_table.get_deliv_time(pack)
                    time_min = str(int(package_table.get_deliv_time(pack))%60)
                    #Formatted time string logic(python datetime was too frustrating)
                    if len(time_min) < 2:
                        del_time = ((str(int(time_tot_min)//60) + ":0" + time_min))
                    else:
                        del_time = ((str(int(time_tot_min)//60) + ":" + time_min))
                    print("Package " + str(pack) + ": " + "Delivered at " + del_time + " by truck3 | Due at: " + str(package_duedate) + " | Address: " + str(package_address))
                elif time >= 480:
                    print("Package " + str(pack) + ": enroute on truck3 | Due at: " + str(package_duedate) + " | Address: " + str(package_address))
                else:
                    print("Package " + str(pack) + ": at hub | Due at: " + str(package_duedate) + " | Address: " + str(package_address))

            if pack_id in truck2_packs:
                if time >= package_table.get_deliv_time(pack):
                    time_tot_min = package_table.get_deliv_time(pack)
                    time_min = str(int(package_table.get_deliv_time(pack))%60)
                    #Formatted time string logic(python datetime was too frustrating)
                    if len(time_min) < 2:
                        del_time = ((str(int(time_tot_min)//60) + ":0" + time_min))
                    else:
                        del_time = ((str(int(time_tot_min)//60) + ":" + time_min))
                    print("Package " + str(pack) + ": " + "Delivered at " + del_time + " by truck2 Due at: " + str(package_duedate) + " Address: " + str(package_address))
                elif time >= 667:
                    print("Package " + str(pack) + ": enroute on truck2 Due at: " + str(package_duedate) + " Address: " + str(package_address))
                else:
                    print("Package " + str(pack) + ": at hub Due at: " + str(package_duedate) + " Address: " + str(package_address))

def create_truck(truck_num, driver="no_driver"):
    '''creates an instance of the Truck class'''
    truck = Truck(truck_num, driver)
    return truck

def load_truck(truck, *args):
    '''Function to load a truck with packages.
    truck: truck object
    args: package numbers to manually load.'''
    #Truck Capapacity
    capacity = 16

    #Logic block to manually load any included packages
    #If there are no manually loaded packages, default address is set to hub address
    if len(args) == 0:
        last_pack_address = '4001 South 700 East'

    else:
        last_package = 0
        for arg in args:
            #Decrement capacity to reflect adding a package
            capacity-=1
            #Utilize truck class to add package
            truck.add_package(arg)
            #Remove pack from pack lists
            special_packs.remove(arg)
            #Set last_package as arg
            last_package = arg
        #Set last package address to the address of the last manually added package
        last_pack_address = package_table.find_package_address(last_package)
    #logic to load the truck to capacity using a version of the nearest neighbor algorithm

    while capacity > 0 and len(package_list) > 0:

        min_dist = 100
        new_pack = package_list[0]
        #Iterates through each remaining package to find the package closest to the last
        #Added package utilizing minimum logic.
        for pack in package_list:
            new_pack_address = package_table.find_package_address(pack)
            new_dist = find_distance(distance_table, last_pack_address, new_pack_address)

            if new_dist < min_dist:
                min_dist = new_dist
                new_pack = pack
        #Adds the closest package
        truck.add_package(new_pack)
        #Updates last address
        last_package_address = new_pack_address
        #Removes package from list
        package_list.remove(new_pack)
        #Decrements truck capacity
        capacity -= 1

def spec_load_truck(truck, *args):
    '''Function to load a truck with packages only loading with manually
    added packages'''
    capacity = 16
    last_package = 0
    #Error logic if truck is overfilled
    if capacity > 0:
        for arg in args:
            capacity-=1
            truck.add_package(arg)
            special_packs.remove(arg)
            last_package = arg
    else:
        print("Error: Truck Full!!!")
        sys.exit(1)

def get_truck_route(truck, pack_list):
    '''Function to create a truck route that satisfies all package and company
     requirements using a trucks pack_list'''
    #Instantiate needed variables
    curr_address = '4001 South 700 East'
    truck_route = []
    route_dist = 0.0
    #Lines 293-344: Logic to find packages with early delivery times and
    #Add them first to satisfy delivery requirements
    for pack in pack_list:
        if pack == 15:
            #Adds package to truck route
            truck_route.append(pack)
            #Removes package from pack_list
            pack_list.remove(pack)
            #Gets distance from current address and adds that to the route distance
            pack_address = package_table.find_package_address(pack)
            dist = find_distance(distance_table, curr_address, pack_address)
            route_dist += dist
            #Updates current address
            curr_address = pack_address
    for pack in pack_list:
        if pack == 25:
            truck_route.append(pack)
            pack_list.remove(pack)
            pack_address = package_table.find_package_address(pack)
            dist = find_distance(distance_table, curr_address, pack_address)
            route_dist += dist
            curr_address = pack_address
    for pack in pack_list:
        if pack == 26:
            truck_route.append(pack)
            pack_list.remove(pack)
            pack_address = package_table.find_package_address(pack)
            dist = find_distance(distance_table, curr_address, pack_address)
            route_dist += dist
            curr_address = pack_address
    for pack in pack_list:
        if pack == 6:
            truck_route.append(pack)
            pack_list.remove(pack)
            pack_address = package_table.find_package_address(pack)
            dist = find_distance(distance_table, curr_address, pack_address)
            route_dist += dist
            curr_address = pack_address
    list_10 = []
    #If the package is in the list of those due by 10:30, add to a list used by a nearest neighbor algorithm.
    for pack in pack_list:
        list_1030 = [1, 21, 19, 4, 29, 30, 31, 34, 37, 40, 14, 16, 20, 30, 31, 34, 37, 40]
        if pack in list_1030:
            list_10.append(pack)
    for pack in list_10:
        while len(list_10) > 0:
            min_dist = 100
            for pack in list_10:
                new_pack_address = package_table.find_package_address(pack)
                new_dist = find_distance(distance_table, curr_address, new_pack_address)

                if new_dist < min_dist:
                    min_dist = new_dist
                    new_pack = pack
            truck_route.append(new_pack)
            pack_list.remove(new_pack)
            list_10.remove(new_pack)
            route_dist += new_dist
            curr_address = new_pack_address

    #After dealing with any extraneous delivery due times, create the remainder of the
    #truck route efficiently by utilizing a similar nearest neighbor algorithm to the ones
    #used before.
    while len(pack_list) > 0:
        min_dist = 100
        for pack in pack_list:
            new_pack_address = package_table.find_package_address(pack)
            if new_pack_address == curr_address:
                new_dist = 0.0
                new_pack = pack
            else:
                new_dist = find_distance(distance_table, curr_address, new_pack_address)

                if new_dist < min_dist:
                    min_dist = new_dist
                    new_pack = pack
        truck_route.append(new_pack)
        pack_list.remove(new_pack)
        route_dist += new_dist
        curr_address = new_pack_address
    #Returns a specifically ordered list of packages as a truck_route
    return truck_route

def deliv_pack(truck, time, travel_time, pack_id, dist: float):
    '''Function to perform the necessary actions to "deliver" a package'''
    #set the delivery truck and add the delivery distance to the truck object.
    del_truck = truck
    del_truck.add_distance(dist)
    #Find package
    package = Package(package_table.find_package(pack_id))
    truck_number = truck.return_truck_num()
    #Update packages delivery status with a truck number and delivery time
    deliv_status = ("Delivered by truck" + str(truck_number) +
                    " at " + str(time))
    package.update_status(deliv_status)
    package_table.update_package(package.get_packageId(), package)

def deliv_time(truck, depart_time, time):
    '''Function to calculate a packages delivery time'''
    dep_time = depart_time
    delivery_time = dep_time + time
    return delivery_time

def run_truck_route(truck, truck_route, depart_time=480):
    '''Function that simulates all actions taken by a truck runnning a truck route.
    depart time is in minutes(the default of 480 indicates a departure time of 8:00 AM'''

    curr_address = '4001 South 700 East'
    truck_travel_time = 0.0
    while len(truck_route) > 0:
        #Algorithm simply runs through the truck route in order of the list
        for pack in list(truck_route):
            new_pack_address = package_table.find_package_address(pack)
            #If logic to deliver multiple packages to one location
            if new_pack_address == curr_address:
                dist = 0.0
            #Logic to obtain distance to deliver a package
            else:
                dist = find_distance(distance_table, curr_address, new_pack_address)
            #Determine travel time based on distance(divided by miles per minute 18/60)
            travel_time_min = dist/(0.3)
            #Add travel time to total truck travel time and obtain delivery time
            truck_travel_time += travel_time_min
            delivery_time = deliv_time(truck, depart_time, truck_travel_time)
            del_min = str(int(delivery_time)%60)
            #Formatted time string logic(python datetime was too frustrating)
            if len(del_min) < 2:
                del_time = ((str(int(delivery_time)//60) + ":0" + del_min))
            else:
                del_time = ((str(int(delivery_time)//60) + ":" + del_min))
            #Deliver package
            deliv_pack(truck, del_time, truck_travel_time, pack, dist)
            truck_route.remove(pack)
            truck.deliver_package(pack)
            #Update address
            curr_address = new_pack_address
            #print("package " + str(pack) + " delivered at:  " + del_time)
    #Calculate distance back to hub and update truck travel distance and time
    ret_dist = find_distance(distance_table, curr_address, '4001 South 700 East')
    travel_time_min = dist/(0.3)
    truck.add_distance(ret_dist)
    truck_travel_time += travel_time_min
    #print("Truck" + str(int(truck.return_truck_num())) + " Total miles driven:" + str(int(truck.get_distance())))
    truck_rettime = truck_travel_time
    #Utilizes deliv_time function to calculate trucks return time
    truck_return_time = deliv_time(truck, depart_time, truck_travel_time)
    #Updates trucks distance travelled with route distance
    truck.set_tripLength(truck_travel_time)
    #print("Route completed in: " + str(int(truck.get_tripLength())) + " minutes")
    truck_rettime_min = str(int(truck_return_time)%60)
    '''if len(truck_rettime_min) < 2:
        return_time = ((str(int(truck_return_time)//60) + ":0" + truck_rettime_min))
    else:
        return_time = ((str(int(truck_return_time)//60) + ":" + truck_rettime_min))
    #print("Truck" + str(int(truck.return_truck_num())) + " Trip completed at " + return_time)
    #if len(truck.get_packages()) > 0:
        #print("Packages: " + str(truck.get_packages()) + " not delivered!!!")
    #else:
        #print("All packages delivered!!!")'''
    #Returns truck travel distance for easier incorporation to interface.
    return truck.get_distance()

def main():
    '''Main function: Houses user interface'''
    #Get total distance travelled by all trucks
    tot_miles_trav = deliver_packages()
    user_int = 0
    #User input logic to implement basic UI
    while user_int != 4:
        #UI options
        print("Options: \n 1: Get all Package info and Total Truck Mileage "
              "\n 2: get a specific package status at a Time"
              "\n 3: get all package status at a Time"
              "\n 4: exit program")
        #Input validation
        while True:
            try:
                user_int = int(input("Select an Option: "))
                if user_int > 0 and user_int < 5:
                    break
                else:
                    print("Not an option. Please input 1, 2, 3, or 4")
                    False
            except ValueError:
                print("Not an option. Please input 1, 2, 3, or 4")
                False
        #Prints all package info and total miles driven
        if user_int==1:
            print("PackageId | Address | City | State | Zip | DeadLine | Weight | Status |")
            package_table.print_pack_status()
            print("Total miles driven by all trucks: " + str(tot_miles_trav))

        #Obtains time from user and prints all package status at that time
        elif user_int==3:

            while True:
                #Time input validation
                try:
                    user_time = input("Enter time (military (i.e. 1:00 PM = 13:00, 9:00 AM = 9:00, etc): ")
                    #Converting time to minutes
                    if len(user_time) == 5:
                        user_hr = int(user_time[0:2])
                        user_min = int(user_time[3:])
                        break
                    elif len(user_time) == 4:
                        user_hr = int(user_time[0])
                        user_min = int(user_time[2:])
                        break
                    else:
                        print("Please enter a time in the specified format!\n"
                              "Hint: Check for any excess spaces.")
                        False
                except ValueError:
                    print("Please enter a time in the specified format!\n")
                    False
            user_time_min = user_hr * 60 + user_min
            #Calling package data function with user time
            get_packageData_atTime(user_time_min, 0)

        #Obtains time and package id from user and prints package status at that time
        elif user_int==2:
            "input validation for package id"
            while True:
                try:
                    user_pack = int(input("Enter package Id: "))
                    if user_pack > 0 and user_pack < 41:
                        break
                    else:
                        print("Please enter a valid package Id (1-40)")
                        False
                except ValueError:
                    print("Please enter a number between 1 and 40!\n")
                    False
            #Input validation for time
            while True:
                try:
                    user_time = input("Enter time (military (i.e. 1:00 PM = 13:00, 9:00 AM = 9:00, etc): ")
                    if len(user_time) == 5:
                        user_hr = int(user_time[0:2])
                        user_min = int(user_time[3:])
                        break
                    elif len(user_time) == 4:
                        user_hr = int(user_time[0])
                        user_min = int(user_time[2:])
                        break
                    else:
                        print("Please enter a time in the specified format!\n"
                              "Hint: Check for any excess spaces.")
                        False
                except ValueError:
                    print("Please enter a time in the specified format!\n")
                    False
            user_time_min = user_hr * 60 + user_min
            #Package info function with specific package
            get_packageData_atTime(user_time_min, user_pack)
        #Exits program
        elif user_int==4:
            print("Exiting Program. Have a nice day!")
            sys.exit(0)
        #Catch statement
        else:
            print("Critical Error! Program Terminated.")
            sys.exit(1)
            return

def deliver_packages():
    '''Original main function: Performs all necessary functions to deliver all packages'''

    #Create truck objects
    truck1 = create_truck(1, "driver1")
    truck3 = create_truck(3, "driver2")
    truck2 = create_truck(2, "NO_DRIVER")

    truck1_miles = 0.0
    truck2_miles = 0.0
    truck3_miles = 0.0

    #Load all trucks
    load_truck(truck1, 16, 14, 15, 13, 19, 20, 21, 29, 34, 39)
    spec_load_truck(truck2, 3, 6, 18, 36, 38, 25, 26, 30, 31, 11, 23, 40, 4, 1, 37, 32)
    load_truck(truck3, 9, 22, 8, 28)

    #Get all truck routes
    truck2_route1 = get_truck_route(truck2, truck2.get_packages())
    truck1_route1 = get_truck_route(truck1, truck1.get_packages())
    truck3_route1 = get_truck_route(truck3, truck3.get_packages())

    #Run all truck routes and return travel distances
    truck1_miles += run_truck_route(truck1, truck1_route1)
    truck2_miles += run_truck_route(truck2, truck2_route1, 545)
    truck3_miles += run_truck_route(truck3, truck3_route1, 594)
    '''if len(package_list) == 0:
        print("Deliveries complete!!!")
    else:
        print("Deliveries not completed!!!")
    '''

    tot_miles_trav = int(truck1_miles + truck2_miles + truck3_miles)
    print("All Routes Completed")
    print("Truck1 Miles: " + str(int(truck1_miles)))
    print("Truck2 Miles: " + str(int(truck2_miles)))
    print("Truck3 Miles: " + str(int(truck3_miles)))
    print("Combined Miles Travelled: " + str(int(tot_miles_trav)))

    #Return total trip distance for easy use in UI
    return tot_miles_trav

if __name__ == '__main__':
    main()

