from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    Integer,
    String,
    text,
    TIMESTAMP,
    ForeignKey,
    UniqueConstraint
)

from .database import Base


class Post(Base):
    __tablename__ = "posts"

    id = Column(
        name="id", type_=Integer, primary_key=True, nullable=False, autoincrement=True
    )
    owner_id = Column(
        ForeignKey("users.id", name="FK_users_posts", ondelete="CASCADE"),
        name="owner_id",
        type_=Integer,
        nullable=False,
    )
    title = Column(name="title", type_=String, nullable=False)
    content = Column(name="content", type_=String, nullable=False)
    published = Column(
        name="published", type_=Boolean, nullable=False, server_default="TRUE"
    )
    rating = Column(name="rating", type_=Integer, nullable=True)
    created_at = Column(
        name="created_at",
        type_=TIMESTAMP(timezone=True),
        nullable=False,
        server_default=text("now()"),
    )
    # find commnd to update time when there is an and change tp the row or maybe use
    # UpdatePost shema and create create a default for last_update to current time
    # last_updated = Column(
    #     name="last_updated",
    #     type_=TIMESTAMP(timezone=True),
    #     nullable=False,
    #     server_default=text("now()"),False
    # )


class User(Base):
    __tablename__ = "users"

    id = Column(
        name="id", type_=Integer, nullable=False, primary_key=True, autoincrement=True, unique=True
    )
    email = Column(
        name="email", type_=String, nullable=False, primary_key=True, unique=True
    )
    password = Column(name="password", type_=String, nullable=False)
    first_name = Column(name="first_name", type_=String, nullable=False)
    last_name = Column(name="last_name", type_=String, nullable=False)
    other_name = Column(name="other_name", type_=String, nullable=True)
    created_at = Column(
        name="created_at",
        type_=TIMESTAMP(timezone=True),
        nullable=False,
        server_default=text("now()"),
    )
    # last_updated = Column(
    #     name="last_updated",
    #     type_=TIMESTAMP(timezone=True),
    #     nullable=False,
    #     server_default=text("now()"),False
    # )


class Vote(Base):
    __tablename__ = "votes"
    post_id = Column(
        ForeignKey("posts.id", ondelete="CASCADE", name="FK_posts_votes"),
        name="post_id",
        type_=Integer,
        primary_key=True,
        nullable=False,
    )
    user_id = Column(
        ForeignKey("users.id", ondelete="CASCADE", name="FK_users_votes"),
        name="user_id",
        type_=Integer,
        primary_key=True,
        nullable=False,
    )
