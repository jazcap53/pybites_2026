from script import Vehicle, Car, Motorbike


def test_vehicle_description():
    v = Vehicle("Generic", "ModelX", 4)
    assert v.description() == "Generic ModelX with 4 wheels"


def test_car_inherits_vehicle():
    c = Car("Toyota", "Corolla", 4, 4)
    assert c.brand == "Toyota"
    assert c.model == "Corolla"
    assert c.wheels == 4
    assert c.doors == 4
    assert c.honk() == "Beep beep!"
    assert c.description() == "Toyota Corolla with 4 wheels"


def test_motorbike_inherits_vehicle():
    m = Motorbike("Yamaha", "R3", 2, 321)
    assert m.brand == "Yamaha"
    assert m.model == "R3"
    assert m.wheels == 2
    assert m.engine_cc == 321
    assert m.rev_engine() == "Yamaha R3 with 2 wheels goes Vroom vroom!"
    assert m.description() == "Yamaha R3 with 2 wheels"
