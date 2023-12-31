"""empty message

Revision ID: 902bd069c275
Revises: a9b157b96c44
Create Date: 2023-09-02 10:49:33.359576

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '902bd069c275'
down_revision = 'a9b157b96c44'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('message', schema=None) as batch_op:
        batch_op.add_column(sa.Column('content', sa.String(length=1000), nullable=False))
        batch_op.drop_column('body')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('message', schema=None) as batch_op:
        batch_op.add_column(sa.Column('body', mysql.VARCHAR(length=1000), nullable=False))
        batch_op.drop_column('content')

    # ### end Alembic commands ###
