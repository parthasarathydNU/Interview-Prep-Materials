from Entities.Rider import Rider
from Entities.Driver import Driver
from Enums.Rating import Rating
from EntityManagerSingletonClasses.RiderManager import RiderManager
from EntityManagerSingletonClasses.DriverManager import DriverManager
from EntityManagerSingletonClasses.TripManager import TripManager
from Entities.Location import Location
import sys
import os

class Uber:
    @staticmethod
    def main():

        sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

        # Your main logic goes here
        print("Main method is running")
        keerthi = Rider(name="Keerthi", rating=Rating.TWO_STARS)
        gaurav = Rider(name="Gaurav", rating=Rating.FIVE_STARS)

        riderManager = RiderManager.get_instance()
        riderManager.addRider(keerthi)
        riderManager.addRider(gaurav)

        yogithaDriver = Driver(name="Yogitha")
        riddhiDriver = Driver(name="Riddhi")

        driverManager = DriverManager.get_instance()
        driverManager.addDriver(yogithaDriver)
        driverManager.addDriver(riddhiDriver)

        tripManager = TripManager.get_instance()

        tripManager.createTrip(
            keerthi, Location(name="Chennai"), Location(name="Bangalore")
        )

        tripManager.createTrip(
            gaurav, Location(name="Mumbai"), Location(name="Thane")
        )

        for tripId in tripManager.tripsMap:
            tripManager.tripsMap[tripId].displayTripDetails()



    @classmethod
    def run(cls):
        cls.main()

if __name__ == "__main__":
    Uber.run()
