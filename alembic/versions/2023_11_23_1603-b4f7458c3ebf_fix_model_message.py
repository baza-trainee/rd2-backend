"""fix model message

Revision ID: b4f7458c3ebf
Revises: dc0a3ebbbb12
Create Date: 2023-11-23 16:03:04.701321

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b4f7458c3ebf'
down_revision: Union[str, None] = 'dc0a3ebbbb12'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('messages', sa.Column('msg', sa.Text(), nullable=True))
    op.drop_column('messages', 'description')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('messages', sa.Column('description', sa.TEXT(), autoincrement=False, nullable=True))
    op.drop_column('messages', 'msg')
    # ### end Alembic commands ###
