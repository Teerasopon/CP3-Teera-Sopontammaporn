class Vehicle():
    licenseCode = ""
    serialCode = ""
    def turnOnAirConditioner(self):
        print("Turn on : Air")


class Car(Vehicle):
    def sayHello(self):
        print("Hello world")

class PickUp(Vehicle):
    pass

class Van(Vehicle):
    pass

class Estatecar(Vehicle):
    pass


car1 = Car()
car1.turnOnAirConditioner()
PickUp1 = PickUp()
PickUp1.turnOnAirConditioner()
Van1 = Van()
Van1.turnOnAirConditioner()
Estatecar1 = Estatecar()
Estatecar1.turnOnAirConditioner()
