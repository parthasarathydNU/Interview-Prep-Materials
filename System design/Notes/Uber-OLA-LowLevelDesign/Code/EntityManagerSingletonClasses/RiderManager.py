from Entities.Rider import Rider
import threading
from typing import Optional

from EntityManagerSingletonClasses.SingletonBaseClass import SingletonBaseClass

class RiderManager(SingletonBaseClass):

    # PRIVATE METHODS on class instance
    def initialize(self):
        # Steps required to initialize class instance
        self._ridersMap = dict()
    
    # PUBLIC METHODS on class instance
    def addRider(self,rider: Rider):
        self._ridersMap[rider.name] = rider
        print(f"Rider {rider.name} added to {self.__class__.__name__}")

    def getRider(self, riderName: str) -> Optional[Rider]:
        return self._ridersMap[riderName]
