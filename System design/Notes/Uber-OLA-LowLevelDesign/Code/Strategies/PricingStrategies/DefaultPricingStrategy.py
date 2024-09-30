from InterfaceAPIs.StrategyAPIs import PricingStrategy
from Entities import TripMetaData
from Util.ratingUtil import isHighRating


class DefaultPricingStrategy(PricingStrategy):
    
    def calculatePrice(self, tripMetadata: TripMetaData) -> float:
        """
        Prices rides at $100.0
        """

        defaultPrice = 100.0
        
        print(f"Based on DefaultPricingStrategy the price of the ride is ${defaultPrice}")

        return defaultPrice
