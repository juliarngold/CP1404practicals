from prac_09.car import Car
import random


class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability=0.0):
        """Initialise a UnreliableCar instance."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Attempt to drive a given distance. The car drives the distance if it passes a reliability check and has enough fuel.
    If fuel is insufficient, it drives until fuel runs out. If reliability check fails, the car does not move."""
        if self.reliability > random.randint(0, 100):
            if distance > self.fuel:
                distance = self.fuel
                self.fuel = 0
            else:
                self.fuel -= distance
            self._odometer += distance
        else:
            print("Oops... Something's broken")
        return distance
