from abc import ABC, abstractmethod

import threading

class SingletonBaseClass(ABC):

    _instance = None
    _lock= threading.Lock()

    # Class Methods | Public
    def __init__(self):
        raise RuntimeError('Call get_instance() instead')

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            with cls._lock:

                if cls._instance is None:
                    cls._instance= cls.__new__(cls)
                    cls._instance.initialize()

        return cls._instance
    
    # Instance methods | Private
    @abstractmethod
    def initialize(self, *args, **kwargs) -> None:
        pass
