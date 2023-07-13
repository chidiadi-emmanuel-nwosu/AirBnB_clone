#!/usr/bin/python3
"""
    base_model Module
"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """class BaseModel that defines all common
       attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """class initiasation"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)
        else:
            for k, v in kwargs.items():
                if k in ["created_at", "updated_at"]:
                    v = datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                if k != "__class__":
                    setattr(self, k, v)

    def __str__(self):
        """returns string format of the some class attribute"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """updates the public instance attribute
           updated_at with the current datetime
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """ returns a dictionary containing all
            keys/values of __dict__ of the instance
        """
        new_dict = {}
        for k, v in self.__dict__.items():
            if k in ["created_at", "updated_at"]:
                new_dict[k] = v.isoformat()
            else:
                new_dict[k] = v
        new_dict['__class__'] = self.__class__.__name__
        return new_dict
