class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

class ElectricCar:
    def __init__(self, battery_capacity):
        self.battery_cap = battery_capacity
        
    def charge(self):
        return self.battery_cap
    
    def get_range(self):
        return self.battery_cap * 5

class GasCar:
    def __init__(self, fuel_capacity):
        self.fuel_cap = fuel_capacity
        
    def fuel(self):
        return self.fuel_cap
    
    def get_fuel_range(self):
        return self.fuel_cap * 20

class Hybrid(Vehicle, ElectricCar, GasCar):
    def __init__(self, make, model, year, battery_capacity, fuel_capacity):
        Vehicle.__init__(self, make, model, year)
        ElectricCar.__init__(self, battery_capacity)
        GasCar.__init__(self, fuel_capacity)
        
    def get_total_range(self):
        return ElectricCar.get_range(self) + GasCar.get_fuel_range(self)


car = Hybrid("Toyota", "Prius", 2021, 5, 40)
#
print(car.make, car.model, car.year)
battery_capacity = car.charge()
fuel = car.fuel()
battery_range = car.get_range()
fuel_range = car.get_fuel_range()
total = car.get_total_range()
3

print(f"\tBattery Capacity: {battery_capacity}")
print(f"\tFuel: {fuel} litres")
print(f"\tBattery Range: {battery_range} kms")
print(f"\tFuel Range: {fuel_range} kms.")
print("\tTotal range:", total, "kms")
