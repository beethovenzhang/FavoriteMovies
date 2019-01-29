#!/usr/bin/env python3
"""import all the necessary modules """
from database_setup import User, Item, Category
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

"""Create a new class engine instance."""
engine = create_engine('sqlite:///filmcatalog.db')

"""make the above engine associated with Session objects."""
Session = sessionmaker(bind=engine)

"""Create a Session object."""
session = Session()

user1 = User(
    name='lubo',
    email='lubocsu@gmail.com',
    picture='https://gss0.baidu.com/-vo3dSag_xI4khGko9WTAnF6hhy/'
            'zhidao/pic/item/b03533fa828ba61efd56af434b34970a304e5925.jpg'
)

session.add(user1)
session.commit()

category1 = Category(
    name='Action',
    user=user1
)

session.add(category1)
session.commit()

item1 = Item(
    name='Incredibles2',
    description='Bob Parr (Mr. Incredible) is left to care for the kids while '
                'Helen (Elastigirl) is out saving the world.',
    category=category1,
    user=user1
)

session.add(item1)
session.commit()

print('database populating Completed!')
