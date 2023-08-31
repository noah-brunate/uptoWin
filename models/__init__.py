#!/usr/bin/python3
"""Module defines this folder as a packages"""

from models.engine.fileStorage import FileStorage


storage = FileStorage()
storage.reload()
