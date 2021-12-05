"""add last few columns to posts table

Revision ID: a4490c46c73a
Revises: a19df47f4393
Create Date: 2021-12-05 13:12:18.272181

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a4490c46c73a'
down_revision = 'a19df47f4393'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", 
                  sa.Column("published", sa.Boolean(), nullable=False, server_default="TRUE"),)
    op.add_column("posts", 
                  sa.Column("created_at", sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text("NOW()")),)
    pass


def downgrade():
    op.drop_column("posts", "published")
    op.drop_column("posts", "created_at")
    
    pass
