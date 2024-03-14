# Creating Truck class with states
class Truck:
    def __init__(self, max_fuel_amount, km_per_liter, repair_wheels_price, brand):
        self.max_fuel_amount = int(max_fuel_amount)
        self.km_per_liter = int(km_per_liter)
        self.repair_wheels_price = int(repair_wheels_price)
        self.brand = brand


# Creating Road class with states
class Road:
    def __init__(self, name, terrain_hardness, mental_effect, wheel_damage_effect):
        self.name = name
        self.terrain_hardness = terrain_hardness
        self.mental_effect = mental_effect
        self.wheel_damage_effect = int(wheel_damage_effect)
