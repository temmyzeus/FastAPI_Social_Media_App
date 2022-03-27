"""add title & content to post table

Revision ID: 6c88a6eba5cd
Revises: abb49ba67c47
Create Date: 2022-03-25 08:39:16.564536

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "6c88a6eba5cd"
down_revision = "abb49ba67c47"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column(name="title", type_=sa.String, nullable=False))
    op.add_column("posts", sa.Column(name="content", type_=sa.String, nullable=False))


def downgrade():
    op.drop_column("posts", "title")
    op.drop_column("posts", "content")
