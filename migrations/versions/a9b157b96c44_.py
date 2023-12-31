"""empty message

Revision ID: a9b157b96c44
Revises: 5674141fb1c2
Create Date: 2023-09-01 22:37:39.920382

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'a9b157b96c44'
down_revision = '5674141fb1c2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('message', schema=None) as batch_op:
        batch_op.alter_column('room',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=False)
        batch_op.drop_column('active')

    with op.batch_alter_table('room', schema=None) as batch_op:
        batch_op.alter_column('owner',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('room', schema=None) as batch_op:
        batch_op.alter_column('owner',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)

    with op.batch_alter_table('message', schema=None) as batch_op:
        batch_op.add_column(sa.Column('active', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True))
        batch_op.alter_column('room',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)

    # ### end Alembic commands ###
