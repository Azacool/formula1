from driver import Driver
from grand_prix import GP
from time_formexample1 import TimeForm

class TimeGP:
    def __init__(self,grand_prix:GP,driver:Driver,end_time:TimeForm):
        self._grand_prix=grand_prix
        self._driver=driver
        self._end_time=end_time

    def get_race_time(self):
        return self._end_time
    
    def __str__(self):
        return f"{self._driver.get_name()} finished {self._grand_prix.get_name()} in {self._end_time}"
    

