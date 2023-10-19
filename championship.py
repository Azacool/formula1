from driver import Driver
from grand_prix import GrandPrix

class Championship:
    def __init__(self):
        self.drivers:list[Driver] = []
        self.grand_prix_list:list[GrandPrix] = []

    def create_driver(self, name):
        driver = Driver(name)
        self.drivers.append(driver)
        return driver

    def get_drivers(self):
        return self.drivers

    def get_driver(self, driver_name):
        for driver in self.drivers:
            if driver.get_name() == driver_name:
                return driver
        return None 

    def define_grandprix(self, name):
        grand_prix = GrandPrix(name)
        self.grand_prix_list.append(grand_prix)
        return grand_prix

    def get_grandprix(self, grand_prix_name):
        for grand_prix in self.grand_prix_list:
            if grand_prix.get_name() == grand_prix_name:
                return grand_prix
        return None  
