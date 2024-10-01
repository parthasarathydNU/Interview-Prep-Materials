from Entities.Person import Person
from Enums.Rating import Rating

class Rider(Person):
    
    def __init__(self, name: str, rating: Rating) -> None:
        super().__init__(name)
        self._rating = Rating.UNASSIGNED if rating is None else rating
    
    @property
    def rating(self) -> Rating:
        return self._rating
    
    @rating.setter
    def rating(self, rating: Rating) -> None:
        self._rating = rating
