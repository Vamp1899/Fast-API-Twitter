"""auto-vote

Revision ID: 71c45845e64e
Revises: 56923850b103
Create Date: 2022-06-17 19:23:36.414061

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '71c45845e64e'
down_revision = '56923850b103'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    #op.drop_table('products')
    #op.drop_table('alembic_users')
    #op.drop_table('alembic_posts')
    op.create_table('alembic_votes',
                    sa.Column('user_id', sa.INTEGER(), nullable=False),
                    sa.Column('post_id', sa.INTEGER(), nullable=False),
                    sa.ForeignKeyConstraint(['post_id'], ['alembic_posts.id'],
                                            ondelete='CASCADE'),
                    sa.ForeignKeyConstraint(['user_id'], ['alembic_users.id'],
                                            ondelete='CASCADE'),
                    sa.PrimaryKeyConstraint('user_id', 'post_id')
                    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('alembic_votes')
    # ### end Alembic commands ###
