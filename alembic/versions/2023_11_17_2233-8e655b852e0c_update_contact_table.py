"""update contact table

Revision ID: 8e655b852e0c
Revises: 7d59ca226d10
Create Date: 2023-11-17 22:33:53.291719

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8e655b852e0c'
down_revision: Union[str, None] = '7d59ca226d10'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('contacts', 'post_idx',
               existing_type=sa.INTEGER(),
               type_=sa.String(),
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('contacts', 'post_idx',
               existing_type=sa.String(),
               type_=sa.INTEGER(),
               existing_nullable=False)
    # ### end Alembic commands ###