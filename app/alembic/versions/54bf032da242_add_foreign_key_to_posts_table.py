"""Add foreign key to posts table

Revision ID: 54bf032da242
Revises: 74794ca2bac2
Create Date: 2022-06-17 17:34:18.863284

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '54bf032da242'
down_revision = '74794ca2bac2'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('alembic_posts',sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('posts_user_fk', source_table='alembic_posts',referent_table='alembic_users',local_cols=['owner_id'],remote_cols=['id'],ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint('posts_user_fk', table_name='alembic_posts')
    op.drop_column('alembic_posts', 'owner_id')
    pass
