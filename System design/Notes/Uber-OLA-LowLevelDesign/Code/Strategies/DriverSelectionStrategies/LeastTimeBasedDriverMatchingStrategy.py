from typing import Optional
from Entities.Driver import Driver
from Entities.TripMetaData import TripMetaData
from InterfaceAPIs.StrategyAPIs.DriverMatchingStrategy import DriverMatchingStrategy
from EntityManagerSingletonClasses.DriverManager import DriverManager

class LeastTimeBasedDriverMatchingStrategy(DriverMatchingStrategy):
    
    def matchDriver(self, tripMetadata: TripMetaData) -> Optional[Driver]:    
        """
        Right now we are not implementing any specific logic 
        for demo purpose
        """

        driverManager = DriverManager.get_instance()

        if len(driverManager.getDriversMap()) == 0:
            print("No drivers available")
            return None

        # Gets the first entry from the drivers map
        # Scope to improve
        return next(iter(driverManager.getDriversMap()))


        
        
