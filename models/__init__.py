"""This initializes the storage package"""
from .engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()
