"""create posts table

Revision ID: 698ac1d03b90
Revises: 
Create Date: 2021-12-05 12:09:56.735998

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '698ac1d03b90'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table("posts", sa.Column("id", sa.Integer(), nullable=False, primary_key=True),
                    sa.Column("title", sa.String, nullable=False))
    pass


def downgrade():
    op.drop_table("posts")
    pass
