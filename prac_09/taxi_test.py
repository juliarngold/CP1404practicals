from prac_09.taxi import Taxi

prius = Taxi(100, "Prius 1")

prius.drive(40)

print(prius)

prius.start_fare()

prius.drive(100)

print(prius)

print(prius.current_fare_distance)

print(prius.get_fare())