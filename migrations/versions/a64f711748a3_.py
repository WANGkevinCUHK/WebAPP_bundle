"""empty message

Revision ID: a64f711748a3
Revises: 25782bf9c8b0
Create Date: 2024-05-01 20:49:40.416797

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a64f711748a3'
down_revision = '25782bf9c8b0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('friendship', schema=None) as batch_op:
        batch_op.create_unique_constraint('_src_dst_uc', ['src_id', 'dst'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('friendship', schema=None) as batch_op:
        batch_op.drop_constraint('_src_dst_uc', type_='unique')

    # ### end Alembic commands ###
