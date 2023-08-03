"""Add column to comments table

Revision ID: 8832ca4700ec
Revises: 821be6d388a8
Create Date: 2023-08-03 17:58:05.789113

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8832ca4700ec'
down_revision = '821be6d388a8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('comments', schema=None) as batch_op:
        batch_op.add_column(sa.Column('comment', sa.String(length=1000), nullable=True))
        batch_op.drop_column('content')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('comments', schema=None) as batch_op:
        batch_op.add_column(sa.Column('content', sa.VARCHAR(), nullable=True))
        batch_op.drop_column('comment')

    # ### end Alembic commands ###