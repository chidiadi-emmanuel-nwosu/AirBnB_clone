#!/usr/bin/python3
"""
    user Module
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """review class, inherits form BaseModel"""
    place_id = ""
    user_id = ""
    text = ""
