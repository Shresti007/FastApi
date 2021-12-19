"""add foreign-key to posts table

Revision ID: b1918e71f4ee
Revises: 6321d9961c7c
Create Date: 2021-12-18 11:55:26.466464

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b1918e71f4ee'
down_revision = '6321d9961c7c'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column("owner_id", sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table="posts", referent_table="users",
    local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")

    pass


def downgrade():
    op.drop_constraint("post_users_fk", table_name= "posts")
    op.drop_column('posts', 'owner_id')
    pass
