"""add logos model

Revision ID: c55d33f6ad72
Revises: 985534b682db
Create Date: 2023-11-22 15:33:37.834141

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c55d33f6ad72'
down_revision: Union[str, None] = '985534b682db'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('contacts', 'phone',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('contacts', 'email',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.drop_column('contacts', 'country')
    op.drop_column('contacts', 'post_idx')
    op.drop_column('contacts', 'address')
    op.drop_column('contacts', 'city')
    op.drop_column('contacts', 'street')
    op.alter_column('reports', 'filename',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('reports', 'path',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.create_unique_constraint(None, 'reports', ['path'])
    op.create_unique_constraint(None, 'reports', ['filename'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'reports', type_='unique')
    op.drop_constraint(None, 'reports', type_='unique')
    op.alter_column('reports', 'path',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('reports', 'filename',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.add_column('contacts', sa.Column('street', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.add_column('contacts', sa.Column('city', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.add_column('contacts', sa.Column('address', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.add_column('contacts', sa.Column('post_idx', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.add_column('contacts', sa.Column('country', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.alter_column('contacts', 'email',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('contacts', 'phone',
               existing_type=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###