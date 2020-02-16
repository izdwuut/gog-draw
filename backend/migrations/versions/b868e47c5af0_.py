"""empty message

Revision ID: b868e47c5af0
Revises: 6a50d5d39b0f
Create Date: 2020-02-15 20:52:35.421026

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b868e47c5af0'
down_revision = '6a50d5d39b0f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('steam_users_reddit_comment_id_fkey', 'steam_users', type_='foreignkey')
    op.create_foreign_key(None, 'steam_users', 'reddit_comments', ['reddit_comment_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'steam_users', type_='foreignkey')
    op.create_foreign_key('steam_users_reddit_comment_id_fkey', 'steam_users', 'reddit_comments', ['reddit_comment_id'], ['id'])
    # ### end Alembic commands ###