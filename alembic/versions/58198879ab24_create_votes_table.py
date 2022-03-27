"""create Votes table

Revision ID: 58198879ab24
Revises: b5ba423cf426
Create Date: 2022-03-25 11:56:55.959373

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "58198879ab24"
down_revision = "b5ba423cf426"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "votes",
        sa.Column(
            sa.ForeignKey("posts.id", ondelete="CASCADE", name="FK_posts_votes"),
            name="post_id",
            type_=sa.Integer,
            primary_key=True,
            nullable=False,
        ),
        sa.Column(
            sa.ForeignKey("users.id", ondelete="CASCADE", name="FK_users_votes"),
            name="user_id",
            type_=sa.Integer,
            primary_key=True,
            nullable=False,
        ),
    )


def downgrade():
    op.drop_table("votes")
