"""add index on source passages for files

Revision ID: 61ee53ec45a5
Revises: 9758adf8fdd3
Create Date: 2025-06-20 11:10:02.744914

"""

from typing import Sequence, Union

from alembic import op
from letta.settings import settings

# revision identifiers, used by Alembic.
revision: str = "61ee53ec45a5"
down_revision: Union[str, None] = "9758adf8fdd3"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Skip this migration for SQLite
    if not settings.letta_pg_uri_no_default:
        return

    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index("source_passages_file_id_idx", "source_passages", ["file_id"], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # Skip this migration for SQLite
    if not settings.letta_pg_uri_no_default:
        return

    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index("source_passages_file_id_idx", table_name="source_passages")
    # ### end Alembic commands ###
