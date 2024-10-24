#Creates truck class
import datetime as dt
from PackageTable import PackageTable
from PackageClass import Package

class Truck:
    def __init__(self, truck_num:int, driver = "nodriver"):
        self.truck_num = truck_num
        self.capacity = 16
        self.departure_time = 480
        self.packages = []
        self.route = []
        self.driver = driver
        self.dist_travelled = 0.0
        self.travel_time = 0.0
        self.return_time = self.departure_time

    def set_depart(self, departure_time):
        '''sets depart time'''
        self.departure_time = departure_time

    def get_depart(self):
        '''returns departure time'''
        return self.departure_time

    def set_tripLength(self, route_time):
        '''sets trip length'''
        self.truck_trip_length = route_time

    def get_tripLength(self):
        '''returns trip length'''
        trip_time = self.truck_trip_length
        return trip_time

    def add_travel_time(self, drive_time):
        '''adds travel time'''
        self.travel_time = drive_time + self.travel_time
        self.return_time = self.departure_time + drive_time

    def get_travel_time(self):
        '''returns travel time'''
        return self.travel_time

    def set_return_time(self):
        '''sets return time'''
        self.return_time = self.departure_time + self.travel_time

    def get_return_time(self):
        '''returns return time'''
        return self.return_time

    def add_package(self, package):
        '''adds package'''
        if len(self.packages) < self.capacity:
            self.packages.append(package)
        else:
            print("error: too many packages for truck: " + truck_num)

    def deliver_package(self, pack):
        '''delivers package'''
        key = pack
        #Searches through packages for package id
        for package in self.packages:
            if package[0] == key:
                self.packages.remove(pack)
            else:
                print("error: package not delivered")

    def set_route(self, route):
        '''sets route'''
        self.route = route

    def set_driver(self, driver):
        '''sets driver'''
        self.driver = driver

    def get_packages(self):
        '''returns packages'''
        return self.packages

    def return_truck_num(self):
        '''returns truck num'''
        return self.truck_num

    def add_distance(self, distance):
        '''adds distance'''
        self.dist_travelled += distance

    def get_distance(self):
        '''returns distance'''
        return self.dist_travelled
