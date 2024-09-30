from abc import ABC, abstractmethod
from Entities import TripMetaData, Driver

class DriverMatchingStrategy(ABC):
    @abstractmethod
    def matchDriver(self, tripMetadata: TripMetaData) -> Driver:
        pass    
