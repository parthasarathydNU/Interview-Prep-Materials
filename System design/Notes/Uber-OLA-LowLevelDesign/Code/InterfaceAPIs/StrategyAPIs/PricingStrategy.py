from abc import ABC, abstractmethod
from Entities import TripMetaData

class PricingStrategy(ABC):
    @abstractmethod
    def calculatePrice(self, tripMetadata: TripMetaData) -> float:
        pass
