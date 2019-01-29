#!/usr/bin/env python3
"""import all the necessary modules """
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

"""Construct a base class for declarative class definitions."""
Base = declarative_base()


class User(Base):
    """Class definition of the table user."""

    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))


class Category(Base):
    """Class definition of the table category."""

    __tablename__ = "category"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    item = relationship('Item', cascade='all,delete-orphan')

    @property
    def serialize(self):
        """Return dict format of table data"""

        return {
            'id': self.id,
            'name': self.name,
            'user_id': self.user_id
        }


class Item(Base):
    """Class definition of the table 'item'."""

    __tablename__ = "item"

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    description = Column(String(250))
    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship(Category)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        """Return dict format of table data"""

        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'user_id': self.user_id,
            'category_id': self.category_id
        }


"""Create a new :class:`.Engine` instance."""
engine = create_engine('sqlite:///filmcatalog.db')
"""Create all tables stored in this metadata."""
Base.metadata.create_all(engine)
