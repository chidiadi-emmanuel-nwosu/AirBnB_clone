#!/usr/bin/python3
"""
    file_storage Module
"""
import json
import os


class FileStorage:
    """FileStorage class
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets the __objects"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the
            JSON file (path: __file_path)
        """
        _dict = {k: v.to_dict() for k, v in FileStorage.__objects.items()}

        with open(FileStorage.__file_path, 'w', encoding="utf-8") as f:
            json.dump(_dict, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        objs = {
            'BaseModel': BaseModel,
            'User': User,
            'Place': Place,
            'State': State,
            'City': City,
            'Amenity': Amenity,
            'Review': Review
            }

        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, encoding="utf-8") as f:
                _dict = json.load(f)
            for v in _dict.values():
                self.new(objs[v['__class__']](**v))
