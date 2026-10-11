"""add users table

Revision ID: e3057b7e96d1
Revises: b8100a2a42c6
Create Date: 2026-10-11 12:28:50.550041

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "e3057b7e96d1"
down_revision: Union[str, Sequence[str], None] = "b8100a2a42c6"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "users",
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("email", sa.String(), nullable=False),
        sa.Column("hashed_password", sa.String(), nullable=False),
        sa.Column("first_name", sa.String(), nullable=False),
        sa.Column("last_name", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("user_id"),
        sa.UniqueConstraint("email"),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("users")
