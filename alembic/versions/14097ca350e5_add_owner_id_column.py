"""add owner_id column

Revision ID: 14097ca350e5
Revises: 254c09084f06
Create Date: 2022-03-25 08:56:09.726152

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "14097ca350e5"
down_revision = "254c09084f06"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column(name="owner_id", type_=sa.Integer, nullable=False))


def downgrade():
    op.drop_column("posts", "owner_id")
