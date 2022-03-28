"""make users.id unique(explicit)

Revision ID: 6afcacdbe418
Revises: 6b0fa3d7b800
Create Date: 2022-03-28 11:55:16.110740

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6afcacdbe418'
down_revision = '6b0fa3d7b800'
branch_labels = None
depends_on = None


def upgrade():
    op.create_unique_constraint(constraint_name="UQ_users_id", table_name="users", columns=["id"])


def downgrade():
    op.drop_constraint(constraint_name="UQ_users_id", table_name="users")
