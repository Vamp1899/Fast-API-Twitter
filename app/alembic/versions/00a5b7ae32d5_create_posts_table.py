"""create posts table

Revision ID: 00a5b7ae32d5
Revises: 
Create Date: 2022-06-17 01:39:55.479884

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '00a5b7ae32d5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('alembic_posts', sa.Column('id', sa.Integer(), nullable=True, primary_key=True), sa.Column('title', sa.String(), nullable=True))
    pass


def downgrade():
    op.drop_table('alembic_posts')
    pass
