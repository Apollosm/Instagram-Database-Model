import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    phone = Column(String(250), nullable=False)
    password = Column(String, nullable=False)
    created_at = Column(DateTime)

class Type_post(Base):
    __tablename__ = 'type_post'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))

class Like(Base):
    __tablename__ = 'like'
    id = Column(Integer, primary_key=True)
    id_user = Column(Integer, ForeignKey('user.id'))
    id_post = Column(Integer, ForeignKey('post.id'))
    date = Column(DateTime)

class Comment(Base):
    __tablename__ = 'comment'
    text = Column(String(250), primary_key=True)
    id_user = Column(Integer, ForeignKey('user.id'))
    date = Column(DateTime)
    id_post = Column(Integer, ForeignKey('post.id'))

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    id_user = Column(Integer, ForeignKey('user.id'))
    date = Column(DateTime)
    id_type_post = Column(Integer, ForeignKey('type_post.id'))
    text = Column(String)
    id_post_shared = Column(Integer, ForeignKey('post.id'))

    #def to_dict(self):
        #return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')