Author: Amir Abu Hani

This project is consists from 5 moduls to achieve the truck simulation.

The truck_road_classes module contain the truck and the road classes, which we will use for creating objects in the
simulator module.

The creating_roads.json module will include the road(type and length) that the user can add to be in simulation.

In the roads_data module, we load the data from json and return it as list of dictionaries. I decide to use this module
because later in the utils module,  we can use it for extendability.

In fact, the utils module is maintaining the extendability. By using importlib, we import the roads_data module and
the load_road function that exists in the module.

The last part is the simulator module. In this module, we create one truck and four basic road. then we load by utils 
module the road that the user add to the creating_road module. In accordance to the road type, we sum the details.
