#!/usr/bin/env python3
"""import all the necessary modules """
from database_setup import User, Item, Category
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

"""Create a new class engine instance."""
engine = create_engine('sqlite:///moviecatalog.db')

"""make the above engine associated with Session objects."""
Session = sessionmaker(bind=engine)

"""Create a Session object."""
session = Session()

user1 = User(
    name='Yunfei',
    email='beethovenzhang@gmail.com',
    picture=''
)

session.add(user1)
session.commit()

category1 = Category(
    name='Science Fiction',
    user=user1
)

session.add(category1)
session.commit()

item1 = Item(
    name='The Avengers',
    description='Earth mightiest heroes must come together and learn to'
                'fight as a team if they are going to stop the mischievous'
                'Loki and his alien army from enslaving humanity. ',

    category=category1,
    user=user1
)

session.add(item1)
session.commit()

print('database populating Completed!')
