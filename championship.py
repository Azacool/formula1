from driver import Driver
from grand_prix import GP
from time_gpexample1 import TimeGP

class Championship:
    def __init__(self):
        self.drivers:list[Driver] = []
        self.grand_prix_list:list[GP]= []
        self._end_time_list:list[TimeGP]=[]
    

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
        grand_prix = GP(name)
        self.grand_prix_list.append(grand_prix)
        return grand_prix

    def get_grandprix(self, grand_prix_name):
        for grand_prix in self.grand_prix_list:
            if grand_prix.get_name() == grand_prix_name:
                return grand_prix
        return None  


    def get_championship_ranking(self):
        driver_points = {}
        for grand_prix in self.grand_prix_list:
            for time_gp in grand_prix._race_results:
                driver = time_gp._driver
                points = grand_prix.get_points(driver)
                if driver in driver_points:
                    driver_points[driver] += points
                else:
                    driver_points[driver] = points

        sorted_drivers = sorted(driver_points.keys(), key=lambda driver: driver_points[driver], reverse=True)
        return sorted_drivers
