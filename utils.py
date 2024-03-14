from importlib import import_module


# This function Dynamically import the road module
def load_road(truck, road_module_name):
    try:
        road_module = import_module(road_module_name)
    except ImportError:
        print(f"Error: Module '{road_module_name}' not found.")
        return False
    else:
        # Load roads using the module's load_roads_from_json function
        roads = road_module.load_roads_from_json()
        return roads

