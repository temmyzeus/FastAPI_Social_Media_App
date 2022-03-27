"""add published, rating & created_at columns

Revision ID: 254c09084f06
Revises: 6c88a6eba5cd
Create Date: 2022-03-25 08:49:48.570942

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "254c09084f06"
down_revision = "6c88a6eba5cd"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        "posts",
        sa.Column(
            name="published", type_=sa.Boolean, nullable=False, server_default="TRUE"
        ),
    )
    op.add_column("posts", sa.Column(name="rating", type_=sa.Integer, nullable=True))
    op.add_column(
        "posts",
        sa.Column(
            name="created_at",
            type_=sa.TIMESTAMP(timezone=True),
            nullable=False,
            server_default=sa.text("now()"),
        ),
    )


def downgrade():
    op.drop_column("posts", "published")
    op.drop_column("posts", "rating")
    op.drop_column("posts", "created_at")
