import json


# This function take the creating_roads json and return all roads in it as dictionaries
def load_roads_from_json():
    with open("creating_roads.json", "r") as roads_file:
        roads = json.load(roads_file)
    return roads
