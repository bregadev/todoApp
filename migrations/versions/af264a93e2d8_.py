"""empty message

Revision ID: af264a93e2d8
Revises: 0162ac8b160c
Create Date: 2019-10-26 12:41:28.299527

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'af264a93e2d8'
down_revision = '0162ac8b160c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('todos', sa.Column('completed', sa.Boolean(), nullable=True))

    op.execute('UPDATE todos SET completed = False WHERE completed IS NULL;')

    op.alter_column('todos', 'completed', nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('todos', 'completed')
    # ### end Alembic commands ###
