#!/usr/bin/python3
"""
Initialize models package for FileStorage
"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
