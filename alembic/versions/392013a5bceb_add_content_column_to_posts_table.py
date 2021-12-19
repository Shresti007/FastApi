"""add content column to posts table

Revision ID: 392013a5bceb
Revises: cff4a632672b
Create Date: 2021-12-18 11:19:30.336250

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '392013a5bceb'
down_revision = 'cff4a632672b'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')  
    pass
