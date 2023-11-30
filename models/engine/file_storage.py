import json
import os
import datetime

class FileStorage:
    def __init__(self):
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self, cls=None):
        if cls:
            # Filter objects based on the provided class
            return {key: obj for key, obj in self.__objects.items() if isinstance(obj, cls)}
        else:
            return self.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        with open(self.__file_path, 'w') as f:
            json.dump({key: obj.to_dict() for key, obj in self.__objects.items()}, f)

    def reload(self):
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                data = json.load(f)
                self.__objects = {}
                for key, obj_dict in data.items():
                    class_name, obj_id = key.split('.')
                    try:
                        cls = globals()[class_name]
                    except KeyError:
                        print(f"KeyError: Class '{class_name}' not found.")
                        continue
                    obj = cls(**obj_dict)
                    self.__objects[key] = obj

    def get(self, cls, id):
        key = "{}.{}".format(cls.__name__, id)
        return self.__objects.get(key)
