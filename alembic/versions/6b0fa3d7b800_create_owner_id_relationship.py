"""create owner_id relationship

Revision ID: 6b0fa3d7b800
Revises: 58198879ab24
Create Date: 2022-03-25 12:35:26.652377

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.orm import relationship

# revision identifiers, used by Alembic.
revision = '6b0fa3d7b800'
down_revision = '58198879ab24'
branch_labels = None
depends_on = None


def upgrade():
    # add a foreign key constraint to owner_id
    op.create_foreign_key(constraint_name="FK_users_posts", source_table="posts", referent_table="users", local_cols=["owner_id"], remote_cols=["id"], ondelete="CASCADE")


def downgrade():
    # remove a foreign key constraint in owner_id
    op.drop_constraint(constraint_name="FK_users_posts", table_name="posts")
