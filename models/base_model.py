from models.engine.file_storage import FileStorage
import uuid
from datetime import datetime

# Create an instance of FileStorage
storage = FileStorage()

class BaseModel:
    storage = storage  # Assign the class attribute to the storage instance

    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()
        # Save the instance using the class attribute
        self.storage.save(self)

    def to_dict(self):
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = getattr(self, 'updated_at', None)
        return obj_dict
