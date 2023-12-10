#!/usr/bin/python3
"""Script creating the BaseModel Class"""
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import models
from datetime import datetime
import uuid


Base = declarative_base()


class BaseModel:
    """BaseModel Class"""
    id = Column(String(60), primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow())
    updated_at = Column(DateTime, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Initializion of BaseModel Class"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != __class__:
                    setattr(self, key, value)
        models.storage.new(self)

    def save(self):
        """Save the new updated time of an object"""
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def delete(self):
        """delete the current instance from the storage"""
        models.storage.delete(self)
        models.storage.save()

    def to_dict(self):
        """Return a dictionary of the class"""
        Base_dict = self.__dict__.copy()
        Base_dict['created_at'] = Base_dict["created_at"].isoformat()
        Base_dict['updated_at'] = Base_dict["updated_at"].isoformat()
        Base_dict["__class__"] = self.__class__.__name__
        Base_dict.pop("_sa_instance_state", None)
        return Base_dict
