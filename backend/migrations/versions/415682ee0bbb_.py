"""empty message

Revision ID: 415682ee0bbb
Revises: 
Create Date: 2020-01-28 10:54:57.024874

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '415682ee0bbb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('reddit_users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('karma', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('reddit_comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('thread', sa.String(), nullable=True),
    sa.Column('author', sa.Integer(), nullable=False),
    sa.Column('comment_id', sa.String(), nullable=True),
    sa.Column('entering', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['author'], ['reddit_users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('steam_users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('reddit_user_id', sa.Integer(), nullable=False),
    sa.Column('steam_id', sa.Integer(), nullable=True),
    sa.Column('level', sa.Integer(), nullable=True),
    sa.Column('public', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['reddit_user_id'], ['reddit_users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('steam_users')
    op.drop_table('reddit_comments')
    op.drop_table('reddit_users')
    # ### end Alembic commands ###
