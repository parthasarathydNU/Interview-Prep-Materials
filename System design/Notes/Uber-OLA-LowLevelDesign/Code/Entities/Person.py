class Person:
    def __init__(self, name: str):
        self._name = name
        print(f"Person {name} created")

    @property
    def name(self):
        return self._name
