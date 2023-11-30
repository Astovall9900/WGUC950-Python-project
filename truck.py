# Truck class with all truck attributes needed
class Truck:
    def __init__(self, speed, miles, current_location, depart_time, packages):
        self.speed = speed  # default 18mph
        self.miles = miles  # miles of travel
        self.current_location = current_location  # where truck is currently on route
        self.time = depart_time  # initialize to depart time
        self.depart_time = depart_time  # time of departure from hub
        self.packages = packages  # package list

    # Stringify the truck class details
    def __str__(self):
        return "%s,%s,%s,%s,%s,%s" % (self.speed, self.miles, self.current_location, self.time, self.depart_time, self.packages)