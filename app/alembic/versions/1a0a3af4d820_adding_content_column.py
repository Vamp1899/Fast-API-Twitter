"""Adding content column

Revision ID: 1a0a3af4d820
Revises: 00a5b7ae32d5
Create Date: 2022-06-17 02:44:56.708699

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1a0a3af4d820'
down_revision = '00a5b7ae32d5'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('alembic_posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('alembic_posts', 'content')
    pass
