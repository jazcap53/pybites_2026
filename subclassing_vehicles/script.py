class Vehicle:
    def __init__(self, brand: str, model: str, wheels: int):
        # TODO: store brand, model, and wheels on self
        pass

    def description(self) -> str:
        """Return a string in the format '<brand> <model> with <wheels> wheels'"""
        pass


class Car(Vehicle):
    def __init__(self, brand: str, model: str, wheels: int, doors: int):
        # TODO: call parent __init__ using super()
        # TODO: store doors
        pass

    def honk(self) -> str:
        """Return 'Beep beep!'"""
        pass


class Motorbike(Vehicle):
    def __init__(self, brand: str, model: str, wheels: int, engine_cc: int):
        # TODO: call parent __init__ using super()
        # TODO: store engine_cc
        pass

    def rev_engine(self) -> str:
        """Return '<parent class's description method> goes Vroom vroom!'"""
        pass
