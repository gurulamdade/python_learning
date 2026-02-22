#color_bag =dict(red="4", green="7", blue="8", yellow="9", cyan="6", magenta="5")
#print(color_bag)


cars = {}
print(cars)

cars["brand"] = "Ford" 
cars["model"] = "Mustang"
cars["year"] = 1964
print(cars)

print(cars["brand"])
del cars["model"]
print(cars)

print("Ford" in cars["brand"])

print(cars.keys())

print(cars.values())

print(cars.items())

print(cars.popitem())
print(cars.pop("brand"))


bikes ={}
bikes_color = {}
bikes["brand"] = "Yamaha"
bikes["model"] = "R15"
bikes_color={"red": "bright red", "blue": "navy blue", "black": "jet black"}
bike_tires = {"front": "90/80-17", "rear": "120/70-17"}
vbikes = bikes.copy()
vbikes.update(bikes_color)
vbikes.update(bike_tires)
print(vbikes)

print(bikes.get("brand_name", "Unknown key"))
