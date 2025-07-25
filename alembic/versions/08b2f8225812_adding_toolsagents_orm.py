"""adding ToolsAgents ORM

Revision ID: 08b2f8225812
Revises: 3c683a662c82
Create Date: 2024-12-05 16:46:51.258831

"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op
from letta.settings import settings

# revision identifiers, used by Alembic.
revision: str = "08b2f8225812"
down_revision: Union[str, None] = "3c683a662c82"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Skip this migration for SQLite
    if not settings.letta_pg_uri_no_default:
        return

    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "tools_agents",
        sa.Column("agent_id", sa.String(), nullable=False),
        sa.Column("tool_id", sa.String(), nullable=False),
        sa.Column("tool_name", sa.String(), nullable=False),
        sa.Column("id", sa.String(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=True),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=True),
        sa.Column("is_deleted", sa.Boolean(), server_default=sa.text("FALSE"), nullable=False),
        sa.Column("_created_by_id", sa.String(), nullable=True),
        sa.Column("_last_updated_by_id", sa.String(), nullable=True),
        sa.ForeignKeyConstraint(
            ["agent_id"],
            ["agents.id"],
        ),
        sa.ForeignKeyConstraint(["tool_id"], ["tools.id"], name="fk_tool_id"),
        sa.PrimaryKeyConstraint("agent_id", "tool_id", "tool_name", "id"),
        sa.UniqueConstraint("agent_id", "tool_name", name="unique_tool_per_agent"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # Skip this migration for SQLite
    if not settings.letta_pg_uri_no_default:
        return

    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("tools_agents")
    # ### end Alembic commands ###
