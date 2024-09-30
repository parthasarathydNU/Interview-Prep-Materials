from InterfaceAPIs.StrategyAPIs import PricingStrategy
from Entities import TripMetaData
from Util.ratingUtil import isHighRating


class RateBasedPricingStrategy(PricingStrategy):
    
    def calculatePrice(self, tripMetadata: TripMetaData) -> float:
        """
        Calculates trip price based on the Riders Rating
        If the rider has high rating than charge them $55
        If not charge them $65
        """

        price = 55.0 if isHighRating(tripMetadata.riderRating) else 65.0

        print(f"Based on the rider rating of {tripMetadata.riderRating} the trip is priced at ${price}")

        return price
