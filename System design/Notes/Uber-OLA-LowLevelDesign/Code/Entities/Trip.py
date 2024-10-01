from uuid import UUID, uuid4
from .Rider import Rider
from .Driver import Driver
from .Location import Location
from InterfaceAPIs.StrategyAPIs.PricingStrategy import PricingStrategy
from InterfaceAPIs.StrategyAPIs.DriverMatchingStrategy import DriverMatchingStrategy

class Trip:
    
    def __init__(self,
    rider: Rider,
    driver: Driver,
    tripStartLocation: Location,
    tripEndLocation: Location,
    tripPrice: float,
    tripPricingStrategy: PricingStrategy,
    driverMatchingStrategy: DriverMatchingStrategy
    ) -> None:
        self._rider = rider
        self._driver = driver
        self._startLocation = tripStartLocation
        self._endLocation = tripEndLocation
        self._price = tripPrice
        self._pricingStrategy = tripPricingStrategy
        self._driverMatchingStrategy = driverMatchingStrategy
        self._id = uuid4()

    @property
    def tripId(self) -> UUID:
        return self._id

    def displayTripDetails(self) -> None:

        print(f"\nTrip id - {self._id}")
        print(f"\nPrice - {self._price}")
        print(f"\nTrip Start Location - {self._startLocation.name}")
        print(f"\nTrip End Location - {self._endLocation.name}")

        
                  
    
