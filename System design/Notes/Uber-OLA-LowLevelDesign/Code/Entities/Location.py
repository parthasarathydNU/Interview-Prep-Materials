class Location:
    
    def __init__(self, name: str) -> None:
        self._name = name
    
    @property
    def name(self) -> str:
        return self._name
