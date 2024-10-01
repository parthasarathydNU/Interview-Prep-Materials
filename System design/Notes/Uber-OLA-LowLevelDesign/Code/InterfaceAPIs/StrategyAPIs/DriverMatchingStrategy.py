from abc import ABC, abstractmethod
from Entities.TripMetaData import TripMetaData
from Entities.Driver import Driver

class DriverMatchingStrategy(ABC):
    @abstractmethod
    def matchDriver(self, tripMetadata: TripMetaData) -> Driver:
        pass    
