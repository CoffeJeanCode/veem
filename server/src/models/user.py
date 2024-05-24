from sqlalchemy import create_engine, Table, Column, Integer, String, ForeignKey, Text, TIMESTAMP, MetaData, Sequence
from sqlalchemy.orm import relationship
from src.config.database import Base, metadata, engine
from datetime import datetime

class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True, index=True)
    username = Column(String(60), unique=True, index=True)
    email = Column(String(100), unique=True, index=True)
    password = Column(String(150))
    created_at = Column(TIMESTAMP, default=datetime.now, nullable=False)


follows = Table(
    'follows', metadata,
    Column('follow_id', Integer, Sequence('follow_id_seq'), primary_key=True),
    Column('follower_id', Integer, ForeignKey('users.user_id'), nullable=False),
    Column('following_id', Integer, ForeignKey('users.user_id'), nullable=False),
    Column('created_at', TIMESTAMP, nullable=False)
)

likes = Table(
    'likes', metadata,
    Column('like_id', Integer, Sequence('like_id_seq'), primary_key=True),
    Column('user_id', Integer, ForeignKey('users.user_id'), nullable=False),
    Column('post_id', Integer, ForeignKey('posts.post_id'), nullable=False),
    Column('created_at', TIMESTAMP, nullable=False)
)

comments = Table(
    'comments', metadata,
    Column('comment_id', Integer, Sequence('comment_id_seq'), primary_key=True),
    Column('user_id', Integer, ForeignKey('users.user_id'), nullable=False),
    Column('post_id', Integer, ForeignKey('posts.post_id'), nullable=False),
    Column('comment', Text, nullable=False),
    Column('created_at', TIMESTAMP, nullable=False)
)

