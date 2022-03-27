"""create_basic_post_table

Revision ID: abb49ba67c47
Revises: 
Create Date: 2022-03-25 07:56:57.745108

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "abb49ba67c47"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "posts",
        sa.Column(
            name="id",
            type_=sa.Integer,
            primary_key=True,
            nullable=False,
            autoincrement=True,
        ),
    )


def downgrade():
    op.drop_table("posts")
