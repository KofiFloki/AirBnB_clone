#!/usr/bin/python3
"""
user subclass  model
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    This is a subclass with user's functionality that inherits from BaseModel
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
