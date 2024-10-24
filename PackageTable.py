#Package Table Class
import sys
from PackageClass import Package

class PackageTable:
    '''Class definition for the package table. Creates
    a hashtable as specified in project requirements to
    allow the use of data functions on the packages.'''
    def __init__(self, starting_size=20):
        '''Starting size of 20 was determined to create an
        optimal hashtable that allows for minimal search time
        due to excessive chaining.'''
        self.table = [] #Creates table
        for i in range(starting_size):
            #Forces Python to create an array of size 20
            self.table.append([])

    def __str__(self):
        for i in range(len(self.table)):
            print(f'{self.table[i]} /n')
        return "done"

    def calc_hash(self, key_value):
        '''Calculates hash value based upon table size
        and package ID.'''
        hash = key_value #Package ID
        return hash % 20 #assign bucket based on ID

    def insert_package(self, key_value, package):
        #Calculates bucket hash using the package ID
        bucket_loc = self.calc_hash(key_value)
        #Pulls list of objects in the given bucket
        bucket_packages = self.table[bucket_loc]
        package_info = [package.get_packageInfo()]
        #Iterates through each bucket looking for
        #The specified package via package ID.
        for item in bucket_packages:
            if item[0] == key_value:
                item[1:] = package_info[1:]
                return True
        bucket_packages.append(package_info)
        return True

    def update_package(self, key_value, package):
        #Calculates bucket hash using the package ID
        bucket_loc = self.calc_hash(key_value)
        #Pulls list of objects in the given bucket
        bucket_packages = self.table[bucket_loc]
        package_info = package.get_packageInfo()
        #Iterates through each bucket looking for
        #The specified package via package ID.
        for item in bucket_packages:
            if item[0][0] == key_value:
                #Replaces package with updated package
                item[0] = package_info
                return True
        print("error updating package")
        return

    def find_package(self, key_value):
        '''Searches hashtable for a package with the given
        key value(package ID)'''
        #Calculates bucket hash using the package ID
        bucket_loc = self.calc_hash(key_value)
        #Pulls list of objects in the given bucket
        bucket_packages = self.table[bucket_loc]
        #Iterates through each bucket looking for
        #The specified package via package ID.

        for item in bucket_packages:
            if item[0][0] == key_value:
                return item[0]


        #If the package is not found, function returns
        #None value
        else:
            return None

    def find_package_address(self, key_value):
        '''Searches hashtable for a package with the given
        key value(package ID)'''
        #Calculates bucket hash using the package ID
        bucket_loc = self.calc_hash(key_value)
        #Pulls list of objects in the given bucket
        bucket_packages = self.table[bucket_loc]
        #Iterates through each bucket looking for
        #The specified package via package ID.

        for item in bucket_packages:
            if item[0][0] == key_value:
                #Returns only package address
                return item[0][1]


        #If the package is not found, function returns
        #None value
        else:
            return None

    def get_packageDueDate(self, key_value):
        '''Searches hashtable for a package with the given
        key value(package ID)'''
        #Calculates bucket hash using the package ID
        bucket_loc = self.calc_hash(key_value)
        #Pulls list of objects in the given bucket
        bucket_packages = self.table[bucket_loc]
        #Iterates through each bucket looking for
        #The specified package via package ID.

        for item in bucket_packages:
            if item[0][0] == key_value:
                #Returns only package address
                return item[0][5]


        #If the package is not found, function returns
        #None value
        else:
            return None

    def get_packageZip(self, key_value):
        '''Searches hashtable for a package with the given
        key value(package ID)'''
        #Calculates bucket hash using the package ID
        bucket_loc = self.calc_hash(key_value)
        #Pulls list of objects in the given bucket
        bucket_packages = self.table[bucket_loc]
        #Iterates through each bucket looking for
        #The specified package via package ID.

        for item in bucket_packages:
            if item[0][0] == key_value:
                #Returns only package address
                return item[0][4]


        #If the package is not found, function returns
        #None value
        else:
            return None

    def get_packageState(self, key_value):
        '''Searches hashtable for a package with the given
        key value(package ID)'''
        #Calculates bucket hash using the package ID
        bucket_loc = self.calc_hash(key_value)
        #Pulls list of objects in the given bucket
        bucket_packages = self.table[bucket_loc]
        #Iterates through each bucket looking for
        #The specified package via package ID.

        for item in bucket_packages:
            if item[0][0] == key_value:
                #Returns only package address
                return item[0][3]


        #If the package is not found, function returns
        #None value
        else:
            return None

    def get_packageCity(self, key_value):
        '''Searches hashtable for a package with the given
        key value(package ID)'''
        #Calculates bucket hash using the package ID
        bucket_loc = self.calc_hash(key_value)
        #Pulls list of objects in the given bucket
        bucket_packages = self.table[bucket_loc]
        #Iterates through each bucket looking for
        #The specified package via package ID.

        for item in bucket_packages:
            if item[0][0] == key_value:
                #Returns only package address
                return item[0][2]


        #If the package is not found, function returns
        #None value
        else:
            return None

    def delete_package(self, key_value):
        '''Searches for package via given package ID
        and removes that package if it is found'''
        #Calculates bucket hash using the package ID
        bucket_loc = self.calc_hash(key_value)
        #Pulls list of objects in the given bucket
        bucket_packages = self.table[bucket_loc]
        #Iterates through each bucket looking for
        #The specified package via package ID.
        for package in bucket_packages:
            #if the package is found, delete package
            if package[0] == key_value:
                self.table[bucket_loc].remove(package)

    def print_pack_status(self):
        '''prints package status'''
        for row in self.table:
            print(row[0])
            print(row[1])

    def get_deliv_time(self, key_value):
        #Calculates bucket hash using the package ID
        bucket_loc = self.calc_hash(key_value)
        #Pulls list of objects in the given bucket
        bucket_packages = self.table[bucket_loc]
        #Iterates through each bucket looking for
        #The specified package via package ID.
        for package in bucket_packages:
            key_value = int(key_value)
            #Searches each package in each bucket and returns time in minutes
            if package[0][0:2] == key_value:
                if len(package[0][7]) == 27:
                    hour = package[0][7][23]
                    min = package[0][7][25:]
                    del_time = int(hour)*60 + int(min)
                    return del_time
                else:
                    hour = package[0][7][23: 25]
                    min = package[0][7][26:]
                    del_time = int(hour)*60 + int(min)
                    return del_time
            elif package[0][0] == key_value:
                if len(package[0][7]) == 27:
                    hour = package[0][7][23]
                    min = package[0][7][25:]
                    del_time = int(hour)*60 + int(min)
                    return del_time
                else:
                    hour = package[0][7][23: 25]
                    min = package[0][7][26:]
                    del_time = int(hour)*60 + int(min)
                    return del_time
            else:
                continue


