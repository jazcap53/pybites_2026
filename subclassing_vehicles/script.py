class Vehicle:
    def __init__(self, brand: str, model: str, wheels: int):
        # TODO: store brand, model, and wheels on self
        self.brand = brand
        self.model = model
        self.wheels = wheels

    def description(self) -> str:
        """Return a string in the format '<brand> <model> with <wheels> wheels'"""
        return f'{self.brand} {self.model} with {self.wheels} wheels'


class Car(Vehicle):
    def __init__(self, brand: str, model: str, wheels: int, doors: int):
        # TODO: call parent __init__ using super()
        # TODO: store doors
        super().__init__(brand, model, wheels)
        self.doors = doors

    def honk(self) -> str:
        """Return 'Beep beep!'"""
        return "Beep beep!"


class Motorbike(Vehicle):
    def __init__(self, brand: str, model: str, wheels: int, engine_cc: int):
        # TODO: call parent __init__ using super()
        # TODO: store engine_cc
        super().__init__(brand, model, wheels)
        self.engine_cc = engine_cc

    def rev_engine(self) -> str:
        """Return '<parent class's description method> goes Vroom vroom!'"""
        return self.description() + " goes Vroom vroom!"
