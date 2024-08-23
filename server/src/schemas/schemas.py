import datetime
import pydantic 

class PostBase(BaseModel):
    image_url: str
    description: str | None = None

class PostCreate(PostBase):
    pass

class Post(PostBase):
    post_id: int
    user_id: int
    created_at: datetime

    class Config:
        orm_mode = True

class CategoryBase(BaseModel):
    name: str

class CategoryCreate(CategoryBase):
    pass

class Category(CategoryBase):
    category_id: int

    class Config:
        orm_mode = True

class PostCategoryBase(BaseModel):
    post_id: int
    category_id: int

class PostCategoryCreate(PostCategoryBase):
    pass

class PostCategory(PostCategoryBase):
    pass

    class Config:
        orm_mode = True

class BoardBase(BaseModel):
    name: str

class BoardCreate(BoardBase):
    pass

class Board(BoardBase):
    board_id: int
    user_id: int
    created_at: datetime

    class Config:
        orm_mode = True

class BoardPostBase(BaseModel):
    board_id: int
    post_id: int

class BoardPostCreate(BoardPostBase):
    pass

class BoardPost(BoardPostBase):
    pass

    class Config:
        orm_mode = True

class LikeBase(BaseModel):
    user_id: int
    post_id: int

class LikeCreate(LikeBase):
    pass

class Like(LikeBase):
    like_id: int
    created_at: datetime

    class Config:
        orm_mode = True

class CommentBase(BaseModel):
    user_id: int
    post_id: int
    comment: str

class CommentCreate(CommentBase):
    pass

class Comment(CommentBase):
    comment_id: int
    created_at: datetime

    class Config:
        orm_mode = True

class FollowBase(BaseModel):
    follower_id: int
    following_id: int

class FollowCreate(FollowBase):
    pass

class Follow(FollowBase):
    follow_id: int
    created_at: datetime

    class Config:
        orm_mode = True

class MoodBoardBase(BaseModel):
    name: str

class MoodBoardCreate(MoodBoardBase):
    pass

class MoodBoard(MoodBoardBase):
    mood_board_id: int
    user_id: int
    created_at: datetime

    class Config:
        orm_mode = True

class MoodBoardPostBase(BaseModel):
    mood_board_id: int
    post_id: int

class MoodBoardPostCreate(MoodBoardPostBase):
    pass

class MoodBoardPost(MoodBoardPostBase):
    pass

    class Config:
        orm_mode = True