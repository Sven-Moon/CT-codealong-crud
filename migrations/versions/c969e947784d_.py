"""empty message

Revision ID: c969e947784d
Revises: b351f2797471
Create Date: 2022-05-25 11:04:24.141186

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c969e947784d'
down_revision = 'b351f2797471'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('animal',
    sa.Column('id', sa.String(length=40), nullable=False),
    sa.Column('species', sa.String(length=50), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('latin_name', sa.String(length=255), nullable=True),
    sa.Column('size_cm', sa.Integer(), nullable=True),
    sa.Column('diet', sa.String(length=255), nullable=True),
    sa.Column('lifespan', sa.String(length=255), nullable=True),
    sa.Column('description', sa.String(length=255), nullable=False),
    sa.Column('image', sa.String(length=100), nullable=True),
    sa.Column('price', sa.Float(precision=2), nullable=False),
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('animal')
    # ### end Alembic commands ###