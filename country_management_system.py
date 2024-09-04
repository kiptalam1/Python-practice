class Country:
    def __init__(self, name, capital, population):
        self.name = name
        self.capital = capital
        self.population = population
        
    def get_info(self):
        return {
            "Name": self.name,
            "Capital": self.capital,
            "Population": self.population
        }


class DevelopedCountry(Country):
    def __init__(self, name, capital, population, gdp):
        super().__init__(name, capital, population)
        self.gdp = gdp
        
    def get_info(self):
        info = super().get_info()
        info["GDP"] = self.gdp
        return info


class DevelopingCountry(Country):
    def __init__(self, name, capital, population, hdi):
        super().__init__(name, capital, population)
        self.hdi = hdi
        
    def get_info(self):
        info = super().get_info()
        info["HDI"] = self.hdi
        return info


class World:
    def __init__(self):
        self.countries = []
        
    def add_country(self, country):
        self.countries.append(country)
        
    def get_country_info(self, name):
        for country in self.countries:
            if country.name == name:
                return country.get_info()
        return None


world = World()
#
kenya = DevelopingCountry("Kenya", "Nairobi", 56432944, 0.598)
usa = DevelopedCountry("United States of America", "Washington, D.C", 331000000, 22512000)
uganda = DevelopingCountry("Uganda", "Kampala", 49000000, 0.550)
#
world.add_country(kenya)
world.add_country(usa)
world.add_country(uganda)
#
country_info = world.get_country_info("Kenya")
#print(country_info) --> prints a dictionary
#
if country_info:
    print("Country info:")
    for key, value in country_info.items():
        print(f"{key}: {value}")
else:
    print("Country not found!")
