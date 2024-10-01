from Entities.Person import Person

class Driver(Person):
    
    def __init__(self, name: str) -> None:
        super().__init__(name)
