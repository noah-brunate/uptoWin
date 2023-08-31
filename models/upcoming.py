#!/usr/bin/python3
"""Module for the Upcoming class"""

from models.basemodel import BaseModel


class Upcoming(BaseModel):
    """the Upcoming class"""
    start_time = ""
    end_time = ""
    name = ""
    url = ""
