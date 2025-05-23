"""fix profile table

Revision ID: b4e830e1f283
Revises: 03972d751223
Create Date: 2025-04-23 11:53:37.787741

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b4e830e1f283'
down_revision: Union[str, None] = '03972d751223'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('profiles', sa.Column('user_id', sa.String(), nullable=False))
    op.create_foreign_key(None, 'profiles', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'profiles', type_='foreignkey')
    op.drop_column('profiles', 'user_id')
    # ### end Alembic commands ###
