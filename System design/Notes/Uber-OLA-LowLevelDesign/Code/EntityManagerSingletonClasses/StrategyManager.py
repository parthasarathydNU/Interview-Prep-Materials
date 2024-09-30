from Entities import TripMetaData
from Strategies.PricingStrategies import RatingBasedPricingStrategy
from Strategies.DriverSelectionStrategies import LeastTimeBasedDriverMatchingStrategy
from InterfaceAPIs.StrategyAPIs import PricingStrategy, DriverMatchingStrategy

import threading

class StrategyManager:

    _instance = None
    _lock= threading.lock()

    # Class Methods | Public
    def __init__(self):
        raise RuntimeError('Call get_instance() instead')

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            with cls._lock:

                if cls._instance is None:
                    cls._instance= cls.__new__(cls)
                    cls._instance._initialize()

        return cls._instance
    
    # Instance methods | Private
    def _initialize(self):
        pass

    # Instance methods | Public
    def determinePricingStrategy(self, tripMetaData: TripMetaData) -> PricingStrategy:
        """
        This method determines the pricing strategy based on the trip metadata. Returns a Pricing Strategy Object
        """
        return RatingBasedPricingStrategy()
    
    def determineDriverMatchingStrategt(self, tripMetadata: TripMetaData) -> DriverMatchingStrategy:
        """
        This method determines the driver matching strategt based on the trip metadata
        """
        return LeastTimeBasedDriverMatchingStrategy()
