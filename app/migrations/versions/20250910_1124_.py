"""empty message

Revision ID: c0e5dbbbcfd6
Revises: cd31d947a7a3, 926b722db0ef
Create Date: 2025-09-10 11:24:08.356329

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c0e5dbbbcfd6'
down_revision: Union[str, Sequence[str], None] = ('cd31d947a7a3', '926b722db0ef')
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
