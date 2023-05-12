#!/usr/bin/python3
"""A subclass city that inherits from BaseModel"""

from models.base_model import BaseModel


class City(BaseModel):
    """City class that is inherited from BaseModel"""

    state_id = ""
    name = ""
