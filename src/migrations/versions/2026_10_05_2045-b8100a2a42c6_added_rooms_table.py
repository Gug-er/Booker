"""added rooms table

Revision ID: b8100a2a42c6
Revises: 5f38c48cb5fc
Create Date: 2026-10-05 20:45:03.713360

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = "b8100a2a42c6"
down_revision: Union[str, Sequence[str], None] = "5f38c48cb5fc"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "rooms",
        sa.Column("room_id", sa.Integer(), nullable=False),
        sa.Column("hotel_id", sa.Integer(), nullable=False),
        sa.Column("title", sa.String(), nullable=False),
        sa.Column("description", sa.String(length=500), nullable=True),
        sa.Column("price", sa.Integer(), nullable=False),
        sa.Column("quantity", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["hotel_id"],
            ["hotels.hotel_id"],
        ),
        sa.PrimaryKeyConstraint("room_id"),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("rooms")
