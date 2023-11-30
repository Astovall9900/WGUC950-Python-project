# TASK C
# Alex Stovall
# 004928444
# WGU C950

# Module imports
import csv
import datetime
import hashTable
import package
import truck


def main():
    # Data aggregation
    # import CSV files for package data into the application
    with open("csvFiles/addressCSV.csv") as address_csv:
        address_raw = csv.reader(address_csv)  # import the address data
        address_data = list(address_raw)  # import it and convert it to an array
    with open("csvFiles/distanceCSV.csv") as distance_csv:
        distance_raw = csv.reader(distance_csv)
        distance_data = list(distance_raw)  # do the same thing for the distance data

    # Create the Hash table for the packages
    package_hash = hashTable.HashTable()

    # Create packages and convert raw data into package info we can use
    def package_creator(file):
        with open(file) as package_raw_data:
            package_info = csv.reader(package_raw_data, delimiter=',')
            next(package_info)
            for pack in package_info:
                package_id = int(pack[0])
                street = pack[1]
                city = pack[2]
                state = pack[3]
                package_zip = pack[4]
                deadline = pack[5]
                weight = pack[6]
                notes = pack[7]
                status = "At the Hub"
                departure_time = None
                delivery_time = None

                # create a package based off of the package class from package.py
                p = package.Package(package_id, street, city, state, package_zip, deadline, weight, notes, status, departure_time,
                             delivery_time)
                # insert into hash table
                package_hash.insert(package_id, p)

    # create the packages based off of the packageCSV
    package_creator('CSVFiles/packageCSV.csv')

    # Helper functions (Address and distance calculations for later)
    # returns the key / identifier of the address from the addressdata
    def find_address(add):
        for row in address_data:
            if add in row[2]:
                return int(row[0])

    # calculate the distance between 2 addresses using the distance matrix csv
    def calc_distance(address1, address2):
        distance = distance_data[address1][address2]
        if distance == '':
            distance = distance_data[address2][address1]
        return float(distance)  # convert to floating point for datetime function

    # Load Trucks and instantiate the truck class
    # setting speed to 18, distance to 0 and address to the starting address of the HUB
    truck1 = truck.Truck(18, 0.0, "4001 South 700 East", datetime.timedelta(hours=8),
                             [1, 13, 14, 15, 16, 19, 20, 27, 29, 30, 31, 34, 37, 40])  # packages have to be delivered together
    truck2 = truck.Truck(18, 0.0, "4001 South 700 East", datetime.timedelta(hours=11),
                             [2, 3, 4, 5, 9, 18, 26, 28, 32, 35, 36, 38])   # packages can only be on truck 2
    truck3 = truck.Truck(18, 0.0, "4001 South 700 East", datetime.timedelta(hours=9, minutes=5),
                             [6, 7, 8, 10, 11, 12, 17, 21, 22, 23, 24, 25, 33, 39])

    # calculations for the actual truck deliveries
    def deliver_packages(vehicle):

        being_delivered = []  # list of packages currently being delivered
        for p in vehicle.packages:
            parcel = package_hash.look_up(p)
            being_delivered.append(parcel)

        vehicle.packages.clear()
        # while there are packages left to be delivered the algorithm will run
        while len(being_delivered):
            next_add_distance = 2000
            next_package = None
            for parcel in being_delivered:
                next_package = parcel
                # if a truck has these priority packages then they must be delivered first / immediately
                if parcel.ID in [25, 6]:
                    next_add_distance = calc_distance(find_address(vehicle.currentLocation), find_address(parcel.street))
                    break
                # go through and find the shortest distance after the current parcel route
                if calc_distance(find_address(vehicle.current_location), find_address(parcel.street)) <= next_add_distance:
                    next_add_distance = calc_distance(find_address(vehicle.current_location), find_address(parcel.street))

            # add current package back to truck and add calculated truck miles and delivery time to totals
            vehicle.packages.append(next_package.ID)
            vehicle.miles += next_add_distance
            vehicle.current_location = next_package.street  # we can locate truck location
            vehicle.time += datetime.timedelta(hours=next_add_distance / 18)

            # package is being delivered here
            next_package.delivery_time = vehicle.time
            next_package.departure_time = vehicle.depart_time

            # package has been delivered so remove from list
            being_delivered.remove(next_package)
            # now go back and start loop to calculate next nearest package

    deliver_packages(truck1)  # delivers packages for truck 1
    deliver_packages(truck3)  # delivers packages for truck 3
    # truck 2 must leave after 1 or 3 since there are only 2 drivers
    truck2.depart_time = min(truck1.time, truck3.time)
    deliver_packages(truck2)  # delivers packages for truck 2

    # Actual application start for user
    print("Western Governors University Parcel Delivery Service!!")
    print("The Total mileage for the route is: " + (truck1.miles + truck2.miles + truck3.miles))

    # Task D
    while True:
        time_raw = input("Enter Time To See Package Delivery Status (HH:MM) or e to exit: ")
        if time_raw.lower() == "e": # allows user to exit
            break

        (h, m) = time_raw.split(":")
        time = datetime.timedelta(hours=int(h), minutes=int(m))
        package_list = range(1, 41)
        try:
            parcel_id = int(input("enter package ID to see specific package, otherwise see all: "))
            pack = package_hash.look_up(parcel_id)
            pack.status_update(time)
            print(str(package))
        except ValueError:
            for p_id in package_list:
                pack = package_hash.look_up(p_id)
                pack.status_update(time)
                print(str(package))
    return


if __name__ == "__main__":
    main()

