import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    location = Column(String(100), nullable=False)
    phone_number=Column (String(20), nullable=False)
    email_address=Column (String(20), nullable=False)
    type_of_client=Column (String(20), nullable=False)
    follower = relationship("followRequest")
    followed = relationship("followRequest")
    emited = relationship("Reaction")

    def create_content():
        pass

    def interaction_message():
        pass

    def login():
        pass

    def like_post():
        pass

class Commerce(User):
    __tablename__ = None
    type_publicity =Column (String(20), nullable=False)
    statistics =Column (String(20), nullable=False)
    monetize =Column (String(20), nullable=False)
    
class People(User):
    __tablename__ = None
    friends =Column (String(20), nullable=False)

class Content(Base):
    __tablename__ = 'content'
    id = Column(Integer, primary_key=True)
    imagen = Column(String(250))
    duration = Column(String(250))
    type_content = Column(String(250), nullable=False)
    description = Column(String(250), nullable=False)
    format = Column(String(250), nullable=False)
    author_id = Column(Integer, ForeignKey('user.id'))
    author = relationship("User")
    discriminator = Column(String(150))
    content_reacted = relationship("Reaction")

    __mapper_args__ = {
        'polymorphic_identity':'content',
        'polymorphic_on':discriminator
        }

    def to_dict(self):
        return {}

class Post(Content):
    __tablename__ = None
    __mapper_args__ = { 'polymorphic_identity': 'post' }
    location_post = Column(String(50), nullable=False)

class Lives(Content):
    __tablename__ = None
    __mapper_args__ = { 'polymorphic_identity': 'lives' }
    location_live = Column(String(50), nullable=False)

class IGTV(Content):
    __tablename__ = None
    __mapper_args__ = { 'polymorphic_identity': 'igtv' }
    conexions = Column(String(50), nullable=False)
    resolutions = Column(String(50), nullable=False)
    statistics2 = Column(String(50), nullable=False)

class Reels(Content):
    __tablename__ = None
    __mapper_args__ = { 'polymorphic_identity': 'reels' }
    music_reels = Column(String(50), nullable=False)
    filters_reels = Column(String(50), nullable=False)
    tendent = Column(String(50), nullable=False)

class Stories(Content):
    __tablename__ = None
    __mapper_args__ = { 'polymorphic_identity': 'stories' }
    music_stories = Column(String(50), nullable=False)
    filters_stories = Column(String(50), nullable=False)

class Reaction (Base):
     __tablename__ = 'reaction'
     id = Column(Integer, primary_key=True)
     type_react = Column(String(50), nullable=False)
     date_time = Column(String(50), nullable=False)
     user_id = Column(Integer, ForeignKey('user.id'))
     content_id = Column(Integer, ForeignKey('content.id'))

class followRequest (Base):
     __tablename__ = 'followrequest'
     id = Column(Integer, primary_key=True)
     approved = Column(String(50), nullable=False)
     date_time = Column(String(50), nullable=False)
     followed_id = Column(Integer, ForeignKey('user.id'))
     follower_id = Column(Integer, ForeignKey('user.id'))



## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e