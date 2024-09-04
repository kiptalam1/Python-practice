class Superhero:
    def __init__(self, name, power):
        self.name = name
        self.power = power
        
    def use_power(self):
        print(f"{self.name} is using {self.power} power.")
        
    def intro_hero(self):
        print(f"I am {self.name} and I have the power {self.power}!")
        
    def save_day(self):
        print(f"{self.name} has saved the day!")
        
    def power_level(self):
        length = len(self.power)
        level = length * 10
        return level


class Flying(Superhero):
    def __init__(self, name, power, speed):
        super().__init__(name, power)
        self.speed = speed
        
    def use_power(self):
        print(f"{self.name} is flying at a speed of {self.speed} miles per hour.")
        
    def calc_distance(self, flight_time):
        distance = self.speed * flight_time
        return distance


batman = Superhero("Batman", "Strength")
batman.intro_hero()
print(batman.power_level())
print()

superman = Flying("Clarke Kent", "Flying", 250)
superman.intro_hero()
print("Power:", superman.power_level())
superman.use_power()
print()

flight_time = 30
attack = superman.calc_distance(flight_time)
print(f"{superman.name} can fly a distance of {attack} miles in {flight_time} hours.")
