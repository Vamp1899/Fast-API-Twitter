"""last few columns

Revision ID: 56923850b103
Revises: 54bf032da242
Create Date: 2022-06-17 18:54:50.307363

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '56923850b103'
down_revision = '54bf032da242'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('alembic_posts', sa.Column('published', sa.Boolean(), nullable=False, server_default = 'TRUE'))
    op.add_column('alembic_posts', sa.Column('created_at',sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('alembic_posts', 'published')
    op.drop_column('alembic_posts', 'created_at')
    pass
