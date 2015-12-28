"""add generic node

Revision ID: 0ef83762cbe7
Revises: None
Create Date: 2015-12-28 17:09:13.119115

"""

# revision identifiers, used by Alembic.
revision = '0ef83762cbe7'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('nodes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('nodes')
    ### end Alembic commands ###