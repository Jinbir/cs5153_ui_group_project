"""empty message

Revision ID: 6c6dda8996fa
Revises: 6aa69e0257f1, d69861c21676
Create Date: 2019-05-04 18:37:07.800988

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6c6dda8996fa'
down_revision = ('6aa69e0257f1', 'd69861c21676')
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('contact', sa.Integer(), nullable=True))
    op.add_column('user', sa.Column('name', sa.String(length=128), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'name')
    op.drop_column('user', 'contact')
    # ### end Alembic commands ###
