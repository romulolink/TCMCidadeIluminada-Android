"""filename

Revision ID: 4e0939a0177a
Revises: 4568153f9481
Create Date: 2015-02-16 13:34:28.614057

"""

# revision identifiers, used by Alembic.
revision = '4e0939a0177a'
down_revision = '4568153f9481'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('protocolo', sa.Column('filename', sa.String(length=255), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('protocolo', 'filename')
    ### end Alembic commands ###
