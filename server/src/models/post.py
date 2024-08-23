from sqlalchemy import create_engine, Table, Column, Integer, String, ForeignKey, Text, TIMESTAMP, MetaData, Sequence
from sqlalchemy.orm import relationship
from src.config.database import Base, metadata, engine
import datetime

posts = Table(
    'posts', metadata,
    Column('post_id', Integer, Sequence('post_id_seq'), primary_key=True),
    Column('user_id', Integer, ForeignKey('users.user_id'), nullable=False),
    Column('image_url', String(255)),
    Column('description', Text, nullable=False),
    Column('created_at', TIMESTAMP, nullable=False)
)

categories = Table(
    'categories', metadata,
    Column('category_id', Integer, Sequence('category_id_seq'), primary_key=True),
    Column('name', String(50), nullable=False)
)

post_categories = Table(
    'post_categories', metadata,
    Column('post_id', Integer, ForeignKey('posts.post_id'), nullable=False, primary_key=True),
    Column('category_id', Integer, ForeignKey('categories.category_id'), nullable=False, primary_key=True)
)

