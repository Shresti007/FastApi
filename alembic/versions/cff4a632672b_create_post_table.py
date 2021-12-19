"""create post table

Revision ID: cff4a632672b
Revises: 
Create Date: 2021-12-18 09:58:00.725302

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cff4a632672b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True), sa.Column('title',sa.String(), nullable=False))
    pass

def downgrade():
    op.drop_table('posts')
    pass
