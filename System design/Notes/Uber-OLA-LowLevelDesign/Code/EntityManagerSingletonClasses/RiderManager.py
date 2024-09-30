import threading
from typing import Optional

class RiderManager:

    # Variables to manage singleton property
    _instance = None
    _lock = threading.lock()

    # Class variables
    _ridersMap = dict()

    # We do not allow calling the constructor
    # To enforce singleton design pattern
    def __init__(self):
        raise RuntimeError('Call get_instance() instead')

    @classmethod
    def get_instance(cls):
        """
        The `classmethod` decorator is used to convert
        a method to a static method

        By default is gets the currentClass object as 
        the first parameters
        """
        if cls._instance is None:
            # initialize the instance here
            # Steps to configure this instance
            
            with cls._lock:
                
                # We check again to ensure this class instance was not initialized
                # by some other thread
                if not cls._instance:
                    cls._instance = cls.__new__(cls)
                    cls._instance._initialize()
                    
        return cls._instance

    # PRIVATE METHODS on class instance
    def _initialize(self):
        # Steps required to initialize class instance
        pass
    
    # PUBLIC METHODS on class instance
    def addRider(self, riderName: str, rider: Rider):
        self._ridersMap[riderName] = rider
        print(f"Rider {riderName} added to {self.__class__.__name__}")

    def getRider(self, riderName: str) -> Optional[Rider]:
        return self._ridersMap[riderName]
