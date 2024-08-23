from sqlalchemy import create_engine, Table, Column, Integer, String, ForeignKey, Text, TIMESTAMP, MetaData, Sequence
from sqlalchemy.orm import relationship
from src.config.database import Base, metadata, engine
import datetime

boards = Table(
    'boards', metadata,
    Column('board_id', Integer, Sequence('board_id_seq'), primary_key=True),
    Column('user_id', Integer, ForeignKey('users.user_id'), nullable=False),
    Column('name', String(100), nullable=False),
    Column('created_at', TIMESTAMP, nullable=False)
)

board_posts = Table(
    'board_posts', metadata,
    Column('board_id', Integer, ForeignKey('boards.board_id'), nullable=False, primary_key=True),
    Column('post_id', Integer, ForeignKey('posts.post_id'), nullable=False, primary_key=True)
)

mood_boards = Table(
    'mood_boards', metadata,
    Column('mood_board_id', Integer, Sequence('mood_board_id_seq'), primary_key=True),
    Column('user_id', Integer, ForeignKey('users.user_id'), nullable=False),
    Column('name', String(100), nullable=False),
    Column('created_at', TIMESTAMP, nullable=False)
)

mood_board_posts = Table(
    'mood_board_posts', metadata,
    Column('mood_board_id', Integer, ForeignKey('mood_boards.mood_board_id'), nullable=False, primary_key=True),
    Column('post_id', Integer, ForeignKey('posts.post_id'), nullable=False, primary_key=True)
)

