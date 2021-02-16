#!/usr/bin/python3
"""class Base Model"""
from datetime import datetime
import uuid


class BaseModel:
    """Clase Base
    """
    
    format_date = '%Y-%m-%dT%H:%M:%S.%f'
    
    def __init__(self, *args, **kwargs):
        """Inicializando atributos públicos en la clase
        id = contiene un identificador único
        created_at = fecha y hora del objeto
        updated_at = fecha de actualización y hora del objeto
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    self.__dict__[key] = datetime.strptime(value, self.format_date)
                elif key == '__class__':
                    pass
                else:
                    self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()


    def __str__(self):
        """
        Returns
            [str]: [information of the class]
        """
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """Update
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns:
            a_dict: containg all information of the class
        """
        cpy_dict = dict(self.__dict__)
        cpy_dict['__class__'] = type(self).__name__

        for key, value in cpy_dict.items():
            if isinstance(value, datetime):
                cpy_dict[key] = value.strftime(self.format_date)

        return cpy_dict
    