"""add phone number column to users table

Revision ID: 69043076f5fa
Revises: 930a274447e1
Create Date: 2021-12-05 15:26:23.669771

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '69043076f5fa'
down_revision = '930a274447e1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('phone_number', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'phone_number')
    # ### end Alembic commands ###
