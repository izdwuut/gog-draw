"""empty message

Revision ID: 9ac4df52f96c
Revises: ae37a7eda941
Create Date: 2020-02-17 12:45:46.886163

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9ac4df52f96c'
down_revision = 'ae37a7eda941'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('steam_users', sa.Column('not_scrapped', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('steam_users', 'not_scrapped')
    # ### end Alembic commands ###
