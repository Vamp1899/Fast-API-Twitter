"""add user table

Revision ID: 74794ca2bac2
Revises: 1a0a3af4d820
Create Date: 2022-06-17 16:37:49.113100

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '74794ca2bac2'
down_revision = '1a0a3af4d820'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('alembic_users',sa.Column('id',sa.Integer(),nullable=False, primary_key=True),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),server_default=sa.text('now()'), nullable=False),
                    sa.UniqueConstraint('email')
                    )
    pass


def downgrade() -> None:
    op.drop_table('alembic_users')
    pass
