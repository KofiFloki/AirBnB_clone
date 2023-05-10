#!/usr/bin/python3
"""Base classmodel
This contains the Base class for the AirBnB clone console.
"""

import uuid
from datetime import datetime
from models import storage 

class BaseModel:

     """
     This class defines all common attributes/methods for other classes.
     """

     def __init__(self, **args, **kwargs):
         """
         initializes BaseModel class
         """
        
        time_format =  %Y-%m-%dT%H:%M:%S.%f
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, time_format
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def __str__(self):
    """returns the string representation of the instance of BaseModel class"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
    
    def save(self):
    """updates public instance attribute updated_at with current datetime"""
        from models import storage
        self.updated_at = datetime.now()
        storage.save()
        
    def to_dict(self):
    """returns dictionary containing all keys/values of __dict__ of the instance"""
        dict_re = self.__dict__.copy()
        dict_re['__class__'] = self.__class__.__name__
        dict_re['created_at'] = self.created_at.isoformat()
        dict_re['updated_at'] = self.updated_at.isoformat()
        return dict_re 
