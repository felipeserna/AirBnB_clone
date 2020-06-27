#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new User --")
my_place = Place()
my_place.city_id = "Cali"
my_place.user_id = "pipelin"
my_place.number_rooms = 4
my_place.number_bathrooms = 3
my_place.maxguest = 6
my_place.price_by_night = 2000
my_place.latitude = 1.5
my_place.longitude = 3.5
my_place.amenity_ids = "pets", "shower"
my_place.save()
print(my_place)
