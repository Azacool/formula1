from championship import Championship
from time_gpexample1 import TimeGP
from time_formexample1 import TimeForm

championship = Championship()

driver1 = championship.create_driver("Azizbek Umarov")
driver2 = championship.create_driver("Abdusattor Jumaev")

grandprix1 = championship.define_grandprix("Toshkent Grand Prix")

end_time1 = TimeForm(1, 30, 15, 500)  
time_gp1 = TimeGP(grandprix1, driver1, end_time1)
grandprix1.add_race_result(time_gp1)

end_time2 = TimeForm(1, 30, 10, 200)  
time_gp2 = TimeGP(grandprix1, driver2, end_time2)
grandprix1.add_race_result(time_gp2)

print("Drivers in the championship:")
for driver in championship.get_drivers():
    print(driver.get_name())

search_driver = championship.get_driver("Azizbek Umarov")
if search_driver is not None:
    print("Found driver:", search_driver.get_name())
else:
    print("Driver not found.")

grandprix = championship.get_grandprix("Toshkent Grand Prix")
if grandprix is not None:
    print("Grand Prix event:", grandprix.get_name())
    print("Race Ranking:")
    for driver in grandprix.get_race_ranking():
        print(driver.get_name(), grandprix.get_position(driver))
else:
    print("Grand Prix not found.")

print("Driver Points:")
for driver in championship.get_championship_ranking():
    points = sum(grandprix.get_points(time_gp1._driver) for grandprix in championship.grand_prix_list)
    print(f"{driver.get_name()}: {points} points")

