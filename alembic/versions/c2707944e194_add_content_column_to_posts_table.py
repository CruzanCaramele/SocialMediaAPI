"""add content column to posts table

Revision ID: c2707944e194
Revises: 698ac1d03b90
Create Date: 2021-12-05 12:33:13.634979

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c2707944e194'
down_revision = '698ac1d03b90'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", 
                  sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column("posts", "content")
    pass
