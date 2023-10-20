from championship import Championship


championship = Championship()

driver1 = championship.create_driver("Azizbek Umarov")
driver2 = championship.create_driver("Abdusattor Jumaev")

grandprix1 = championship.define_grandprix("Monaco Grand Prix")
grandprix2 = championship.define_grandprix("Italian Grand Prix")

print("Drivers in the championship:")
for driver in championship.get_drivers():
    print(driver.get_name())

search_driver = championship.get_driver("Azizbek Umarov")
if search_driver != None:
    print("Found driver:", search_driver.get_name())
else:
    print("Driver not found.")

grandprix = championship.get_grandprix("Monaco Grand Prix")
if grandprix != None:
    print("Grand Prix event:", grandprix.get_name())
else:
    print("Grand Prix not found.")
