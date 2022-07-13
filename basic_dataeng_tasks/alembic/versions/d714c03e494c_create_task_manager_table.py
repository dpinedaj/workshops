"""create task manager table

Revision ID: d714c03e494c
Revises: 
Create Date: 2022-06-29 11:47:39.064033

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd714c03e494c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'tasks_manager',
        sa.Column('id', sa.Integer),
        sa.Column('file_name', sa.String),
        sa.Column('fails', sa.Boolean),
        sa.Column('processing', sa.Boolean),
        sa.Column('error', sa.String),
        sa.Column('host', sa.String)

    )


def downgrade():
    op.drop_table('tasks_manager')
