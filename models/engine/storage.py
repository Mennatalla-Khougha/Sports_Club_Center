#!/usr/bin/python3
"""Create the storage engine"""
from os import getenv
from models.BaseModel import Base, BaseModel
from models.player import Player
from models.sport import Sport
from models.tournament import Tournament
from models.record import Record
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


classes = {
    "Player": Player,
    "Sport": Sport,
    "Tournament": Tournament,
    "Record": Record
    }


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        """Initializing a DBStorage instance."""
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".
                                      format(getenv("USER_MYSQL"),
                                             getenv("PWD_MYSQL"),
                                             getenv("HOST_MYSQL"),
                                             getenv("DB_MYSQL")),
                                      pool_pre_ping=True)
        if getenv("MYSQL_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session"""
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls == clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return (new_dict)

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit the changes to the database"""
        self.__session.commit()

    def rollback(self):
        """rollback the changes to the database"""
        self.__session.rollback()

    def delete(self, obj=None):
        """Delete an object from the database

        Args:
            obj (object, optional): object to be deleted. Defaults to None.
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine,
                                    expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def close(self):
        """call remove() method"""
        self.__session.close()
