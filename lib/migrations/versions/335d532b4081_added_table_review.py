"""Added table Review

Revision ID: 335d532b4081
Revises: 2723e7bbcf91
Create Date: 2024-02-15 14:57:30.117050

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '335d532b4081'
down_revision = '2723e7bbcf91'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('reviews',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ratings', sa.Integer(), nullable=True),
    sa.Column('customer_name', sa.String(), nullable=True),
    sa.Column('restaurant_name', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['customer_name'], ['customers.first_name'], ),
    sa.ForeignKeyConstraint(['restaurant_name'], ['restaurants.name'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reviews')
    # ### end Alembic commands ###