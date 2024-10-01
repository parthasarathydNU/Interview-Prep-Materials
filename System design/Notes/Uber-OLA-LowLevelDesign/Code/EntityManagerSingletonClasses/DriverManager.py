import threading
from typing import Optional
from EntityManagerSingletonClasses.SingletonBaseClass import SingletonBaseClass
from Entities.Driver import Driver

class DriverManager(SingletonBaseClass):

    # PRIVATE METHODS on class instance
    def initialize(self):
        # Steps required to initialize class instance
        self._driversMap = dict()
    
    # PUBLIC METHODS on class instance
    def addDriver(self, driver: Driver):
        self._driversMap[driver.name] = driver
        print(f"Driver {driver.name} added to {self.__class__.__name__}")

    def getDriver(self, driverName: str) -> Optional[Driver]:
        return self._driversMap[driverName]

    def getDriversMap(self) -> dict:
        return self._driversMap
