"""add some fitches

Revision ID: c622213c2c7a
Revises: 9940d5eca707
Create Date: 2023-11-09 22:04:26.729382

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'c622213c2c7a'
down_revision: Union[str, None] = '9940d5eca707'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('admins', sa.Column('is_superuser', sa.Boolean(), nullable=True))
    op.alter_column('users', 'role',
               existing_type=postgresql.ENUM('client', 'superadmin', name='usertypeenum'),
               nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'role',
               existing_type=postgresql.ENUM('client', 'superadmin', name='usertypeenum'),
               nullable=True)
    op.drop_column('admins', 'is_superuser')
    # ### end Alembic commands ###