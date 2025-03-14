"""Increase password column size

Revision ID: 369b6df48ca6
Revises: 799165ee2d54
Create Date: 2025-03-10 15:32:09.388663

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '369b6df48ca6'
down_revision = '799165ee2d54'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_profiles', schema=None) as batch_op:
        batch_op.alter_column('password',
               existing_type=sa.VARCHAR(length=128),
               type_=sa.String(length=256),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_profiles', schema=None) as batch_op:
        batch_op.alter_column('password',
               existing_type=sa.String(length=256),
               type_=sa.VARCHAR(length=128),
               existing_nullable=True)

    # ### end Alembic commands ###
