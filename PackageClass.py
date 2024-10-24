# Creates Package Class

class Package:
    '''Package object'''
    def __init__(self, package):
        '''init function for package: takes list object to create package object'''
        self.package_id = int(package[0])
        self.address = package[1]
        self.city = package[2]
        self.state = package[3]
        self.zip = package[4]
        self.deadline = package[5]
        self.weight = package[6]
        self.status = 'at the hub'

        self.package_info = [self.package_id, self.address, self.city, self.state, self.zip, self.deadline, self.weight, self.status]

    def __str__(self):
        return f'{self.package_info}'

    def update_status(self, status):
        '''updates status'''
        self.status1 = status
        self.package_info = [self.package_id, self.address, self.city, self.state, self.zip, self.deadline, self.weight, self.status1]

    def get_packageAddress(self):
        '''returns address'''
        return self.address

    def get_packageCity(self):
        '''returns city'''
        return self.city

    def get_packageState(self):
        '''returns state'''
        return self.state

    def get_packagZip(self):
        '''returns zip'''
        return self.zip

    def get_packageDeadline(self):
        '''returns deadline'''
        return self.deadline

    def get_packageWeight(self):
        '''returns weight'''
        return self.weight

    def get_packageStatus(self):
        '''returns status'''
        return self.status

    def get_packageId(self):
        '''returns package ID'''
        return self.package_id

    def set_packageInfo(self, package_info_index, info):
        '''sets package info'''
        self.package_info[package_info_index] = info

    def get_packageInfo(self):
        '''returns package info'''
        return self.package_info