"""add auto-vote table

Revision ID: 68e0deefa312
Revises: 88a0cc2fba2d
Create Date: 2021-12-18 12:40:00.084957

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '68e0deefa312'
down_revision = '88a0cc2fba2d'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('votes',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['post_id'], ['posts.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('user_id', 'post_id')
    )
    pass


def downgrade():
    op.drop_table('votes')
    pass
