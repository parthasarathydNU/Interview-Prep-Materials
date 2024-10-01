from EntityManagerSingletonClasses.SingletonBaseClass import SingletonBaseClass
from Entities import TripMetaData
from Strategies.PricingStrategies.RateBasedPricingStrategy import RateBasedPricingStrategy
from Strategies.DriverSelectionStrategies.LeastTimeBasedDriverMatchingStrategy import LeastTimeBasedDriverMatchingStrategy
from InterfaceAPIs.StrategyAPIs.PricingStrategy import PricingStrategy
from InterfaceAPIs.StrategyAPIs.DriverMatchingStrategy import DriverMatchingStrategy

import threading

class StrategyManager(SingletonBaseClass):
    
    # Instance methods | Private
    def initialize(self):
        pass

    # Instance methods | Public
    def determinePricingStrategy(self, tripMetaData: TripMetaData) -> PricingStrategy:
        """
        This method determines the pricing strategy based on the trip metadata. Returns a Pricing Strategy Object
        """
        return RateBasedPricingStrategy()
    
    def determineDriverMatchingStrategt(self, tripMetadata: TripMetaData) -> DriverMatchingStrategy:
        """
        This method determines the driver matching strategt based on the trip metadata
        """
        return LeastTimeBasedDriverMatchingStrategy()
