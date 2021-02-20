#!/usr/bin/python3
"""The class"""
import uuid
from datetime import datetime


class BaseModel:
    """Class BaseModel"""
    format_date = '%Y-%m-%dT%H:%M:%S.%f'

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    
    def __str__(self):
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        dict_ = {}
        dict_.update({'__class__': type(self).__name__})
        for key in self.__dict__:
            if key == ['updated_at', 'created_at']:
                dict_.update({key: datetime.isoformat(getattr(self, key))})
            else:
                dict_.update({key: getattr(self, key)})
        return dict_