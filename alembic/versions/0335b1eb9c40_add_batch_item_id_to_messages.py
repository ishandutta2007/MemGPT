"""Add batch_item_id to messages

Revision ID: 0335b1eb9c40
Revises: 373dabcba6cf
Create Date: 2025-05-02 10:30:08.156190

"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op
from letta.settings import settings

# revision identifiers, used by Alembic.
revision: str = "0335b1eb9c40"
down_revision: Union[str, None] = "373dabcba6cf"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Skip this migration for SQLite
    if not settings.letta_pg_uri_no_default:
        return

    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("messages", sa.Column("batch_item_id", sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # Skip this migration for SQLite
    if not settings.letta_pg_uri_no_default:
        return

    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("messages", "batch_item_id")
    # ### end Alembic commands ###
