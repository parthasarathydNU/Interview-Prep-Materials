from .SingletonBaseClass import SingletonBaseClass
from .RiderManager import RiderManager
from .DriverManager import DriverManager
from Entities.TripMetaData import TripMetaData
from Entities.Trip import Trip
from Entities.Rider import Rider
from Entities.Location import Location
from EntityManagerSingletonClasses.StrategyManager import StrategyManager

class TripManager(SingletonBaseClass):

    def initialize(self) -> None:
        
        self._riderManager = RiderManager.get_instance()
        self._driverManager = DriverManager.get_instance()
        self._tripsMetaDataInfo = dict() # TripId and TripMetadata
        self._tripsInfo = dict() # TripId and Trip

    def createTrip(self, rider: Rider, startLocation: Location, endLocation: Location) -> None:
        
        metaData = TripMetaData(
            startLocation,
            endLocation,
            rider.rating
        )

        strategtManager = StrategyManager.get_instance()
        pricingStrategy = strategtManager.determinePricingStrategy(metaData)
        driverMatchingStrategy = strategtManager.determineDriverMatchingStrategt(metaData)

        driver = driverMatchingStrategy.matchDriver(metaData)

        if driver is None:
            print("Trip not created as no drivers are currently available")
            return

        tripPrice = pricingStrategy.calculatePrice(metaData)

        trip = Trip(
            rider,
            driver,
            startLocation,
            endLocation,
            tripPrice,
            pricingStrategy,
            driverMatchingStrategy
        )

        self._tripsInfo[trip._id] = trip
        self._tripsMetaDataInfo[trip._id] = metaData

    @property
    def tripsMap(self) -> dict:
        return self._tripsInfo
