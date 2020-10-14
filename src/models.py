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
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(80), nullable=False)
    fristname = Column(String(80), nullable=False)
    lastname = Column(String(80), nullable=False)
    email = Column(String(255), nullable=False)
    post = relationship("Post")
    comment = relationship("Comment")
    likes = relationship("Likes")
    followers = relationship("Followers")

class Post(Base):
    __tablename__ = 'post'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    comment = relationship("Comment")
    like = relationship("Likes")

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key = True)
    comment_text = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))

class Likes(Base):
    __tablename__ = 'likes'
    id = Column(Integer, primary_key = True)
    user_from = Column(Integer, ForeignKey('user.id'))
    post_to = Column(Integer, ForeignKey('post.id'))

class Followers(Base):
    __tablename__ = 'followers'
    id = Column(Integer, primary_key = True)
    user_from = Column(Integer, ForeignKey('user.id'))
    user_to = Column(Integer, ForeignKey('user.id'))


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')