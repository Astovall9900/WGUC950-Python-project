import datetime


# Package class for part C. Needs to be able to store the info from the table
class Package:
    def __init__(self, ID, street, city, state, zip,deadline,weight, notes, status,departure_time,delivery_time):
        self.ID = ID  # package ID for hashing and key identification
        self.street = street  # street address of package for distance function
        self.city = city  # city of packagen delivery
        self.state = state  # package state
        self.zip = zip  # package zipcode
        self.deadline = deadline  # delivery deadline
        self.weight = weight  # weight of package
        self.notes = notes  # special notes
        self.status = status  # status of package delivery
        self.departure_time = None  # time of departure
        self.delivery_time = None  # time it needs to be delivered

    # return a string of the package attributes
    def __str__(self):
        return "ID: %s, %-20s, %s, %s,%s, Deadline: %s,%s,%s,Departure Time: %s,Delivery Time: %s" % (self.ID, self.street, self.city, self.state, self.zip, self.deadline, self.weight, self.status, self.departure_time, self.delivery_time)

    # This method will update the status of a package depending on the time entered
    def status_update(self, time_change):
        if self.delivery_time is None:
            self.status = "At the hub"
        elif time_change < self.departure_time:
            self.status = "At the hub"
        elif time_change < self.delivery_time:
            self.status = "Out for delivery"
        else:
            self.status = "Delivered" 
        if self.ID == 9:  # special case package 9 will need to change the address
            if time_change > datetime.timedelta(hours=10, minutes=20):
                self.street = "410 S State St"
                self.zip = "84111"
            else:
                self.street = "300 State St"
                self.zip = "84103"
