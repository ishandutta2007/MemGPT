"""Write source_id directly to files agents

Revision ID: 495f3f474131
Revises: 47d2277e530d
Create Date: 2025-07-10 17:14:45.154738

"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op
from letta.settings import settings

# revision identifiers, used by Alembic.
revision: str = "495f3f474131"
down_revision: Union[str, None] = "47d2277e530d"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Skip this migration for SQLite
    if not settings.letta_pg_uri_no_default:
        return

    # ### commands auto generated by Alembic - please adjust! ###
    # Step 1: Add the column as nullable first
    op.add_column("files_agents", sa.Column("source_id", sa.String(), nullable=True))

    # Step 2: Backfill source_id from files table
    connection = op.get_bind()
    connection.execute(
        sa.text(
            """
        UPDATE files_agents
        SET source_id = files.source_id
        FROM files
        WHERE files_agents.file_id = files.id
    """
        )
    )

    # Step 3: Make the column NOT NULL now that it's populated
    op.alter_column("files_agents", "source_id", nullable=False)

    # Step 4: Add the foreign key constraint
    op.create_foreign_key(None, "files_agents", "sources", ["source_id"], ["id"], ondelete="CASCADE")
    # ### end Alembic commands ###


def downgrade() -> None:
    # Skip this migration for SQLite
    if not settings.letta_pg_uri_no_default:
        return

    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, "files_agents", type_="foreignkey")
    op.drop_column("files_agents", "source_id")
    # ### end Alembic commands ###
