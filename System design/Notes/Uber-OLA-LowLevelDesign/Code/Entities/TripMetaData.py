from Entities.Location import Location
from Enums.Rating import Rating

class TripMetaData:

    def __init__(
        self, 
        sourceLocation: Location,
        destinationLocation: Location,
        riderRating: Rating
        ):
        self._sourceLocation = sourceLocation
        self._destinationLocation = destinationLocation
        self._riderRating = riderRating
        # will be updated later when driver is assigned to the trip
        self._driverRating = Rating.UNASSIGNED


    # Getter and setter for riderRating
    @property
    def riderRating(self) -> Rating:
        return self._riderRating

    # Getter and setter for driverRating
    @property
    def driverRating(self) -> Rating:
        return self._driverRating

    @driverRating.setter
    def driverRating(self, value: Rating):
        self._driverRating = value
