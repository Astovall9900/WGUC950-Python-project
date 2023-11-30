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
        return float(distance)

    # Load Trucks and instantiate the truck class
    # setting speed to 18, distance to 0 and address to the starting address of the HUB
    truck1 = truck.Truck(18, 0.0, "4001 South 700 East", datetime.timedelta(hours=8),
                             [1, 13, 14, 15, 16, 19, 20, 27, 29, 30, 31, 34, 37, 40])
    truck2 = truck.Truck(18, 0.0, "4001 South 700 East", datetime.timedelta(hours=11),
                             [2, 3, 4, 5, 9, 18, 26, 28, 32, 35, 36, 38])
    truck3 = truck.Truck(18, 0.0, "4001 South 700 East", datetime.timedelta(hours=9, minutes=5),
                             [6, 7, 8, 10, 11, 12, 17, 21, 22, 23, 24, 25, 33, 39])

    # calculations for the actual truck deliveries

    # Actual application start for user
    print("Western Governors University Parcel Delivery Service!!")
    print("The Total mileage for the route is: " + (truck1.miles + truck2.miles + truck3.miles))


if __name__ == "__main__":
    main()

