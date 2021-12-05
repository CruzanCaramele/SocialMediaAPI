"""add users table

Revision ID: 4513b2294f08
Revises: c2707944e194
Create Date: 2021-12-05 12:38:00.594588

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4513b2294f08'
down_revision = 'c2707944e194'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table("users",
                    sa.Column("id", sa.Integer(), nullable=False),
                    sa.Column("email", sa.String(), nullable=False),
                    sa.Column("password", sa.String(), nullable=False),
                    sa.Column("created_at", sa.TIMESTAMP(timezone=True),
                              server_default=sa.text("now()"), nullable=False),
                    sa.PrimaryKeyConstraint("id"),
                    sa.UniqueConstraint("email")
                )
    pass


def downgrade():
    op.drop_table("users")
    pass
