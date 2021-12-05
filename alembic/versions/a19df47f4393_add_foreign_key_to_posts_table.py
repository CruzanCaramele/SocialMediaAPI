"""add foreign key to posts table

Revision ID: a19df47f4393
Revises: 4513b2294f08
Create Date: 2021-12-05 13:03:48.099211

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a19df47f4393'
down_revision = '4513b2294f08'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", 
                  sa.Column("owner_id", sa.Integer(), nullable=False))
    op.create_foreign_key("posts_users_fk", 
                          source_table="posts", referent_table="users", local_cols=["owner_id"], 
                          remote_cols=["id"], ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint("post_users_fk", table_name="posts")
    op.drop_column("posts", "owner_id")
    pass
