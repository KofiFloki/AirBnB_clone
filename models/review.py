#!/bin/usr/python3
"""Review module that inherits from BaseModel class"""

from models.base_model import BaseModel


class Review(BaseModel):
    """A Review subclass that inherits from BaseModel"""

    place_id = ""
    user_id = ""
    text = ""
