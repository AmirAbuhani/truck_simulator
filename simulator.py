from utils import load_road
from truck_road_classes import Truck, Road
import time

truck1 = Truck(300, 12, 200, "DAF")
road1 = Road("street", "easy", "concentration", 4)
road2 = Road("rural", "medium", "confusion", 6)
road3 = Road("dirt", "hard", "depression", 9)
road4 = Road("highway", "easy", "calmness", 1)


# This function will determine which road object will be suitable when the user load a road type
def choice_road(road):
    if road == "street":
        return road1
    elif road == "rural":
        return road2
    elif road == "dirt":
        return road3
    elif road == "highway":
        return road4


# This is the simulator
def main():
    road_module_name = "roads_data"
    # here we load the roads_data module with the user road
    roads = load_road(truck1, road_module_name)
    # the final road that the user added, will be start for riding with truck1 if the condition is true
    user_road = roads[-1]
    which_road = choice_road(user_road["road_type"])
    if user_road["length"] < truck1.max_fuel_amount:
        print("Start the ride...")
        time.sleep(3)
        # show the road details
        print(f"This road type is: {which_road.name}")
        print(f"Fuel used in this road is: {round(user_road["length"] / truck1.km_per_liter, 2)} litters ")
        print(f"Damage of the wheels is: {which_road.wheel_damage_effect}")
        print(f"Mental health is: {which_road.mental_effect} ")
        print(f"terrain_hardness is: {which_road.terrain_hardness}")
    else:
        print(f"Truck can not do the {which_road.name} road. there is not enough fuel!")


if __name__ == "__main__":
    main()

# {
#   "road_type": "rural",
#   "length": 50
# },
# {
#   "road_type": "dirt",
#   "length": 30
# },
# {
#   "road_type": "highway",
#   "length": 70
# }
