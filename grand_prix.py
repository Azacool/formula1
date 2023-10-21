from time_gpexample1 import TimeGP


class GP:
    def __init__(self, name):
        self._name = name
        self._race_results = []

    def get_name(self):
        return self._name

    def add_race_result(self, time_gp: TimeGP):
        self._race_results.append(time_gp)

    def get_race_ranking(self):
        self._race_results.sort(key=lambda time_gp: time_gp.get_race_time())
        return [time_gp._driver for time_gp in self._race_results]

    def get_position(self, driver):
        ranking = self.get_race_ranking()
        return ranking.index(driver) + 1

    def get_points(self, driver):
        position = self.get_position(driver)
        if position <= 10:
            points = [25, 18, 15, 12, 10, 8, 6, 4, 2, 1]
            return points[position - 1]
        return 0
