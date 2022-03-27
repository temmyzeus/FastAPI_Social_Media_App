"""Create User table

Revision ID: b5ba423cf426
Revises: 14097ca350e5
Create Date: 2022-03-25 08:58:46.390271

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "b5ba423cf426"
down_revision = "14097ca350e5"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "users",
        sa.Column(
            name="id",
            type_=sa.Integer,
            nullable=False,
            primary_key=True,
            autoincrement=True,
        ),
        sa.Column(name="email", type_=sa.String, nullable=False, unique=True),
        sa.Column(name="password", type_=sa.String, nullable=False),
        sa.Column(name="first_name", type_=sa.String, nullable=False),
        sa.Column(name="last_name", type_=sa.String, nullable=False),
        sa.Column(name="other_name", type_=sa.String, nullable=True),
        sa.Column(
            name="created_at",
            type_=sa.TIMESTAMP(timezone=True),
            nullable=False,
            server_default=sa.text("now()"),
        ),
    )


def downgrade():
    op.drop_table("users")
