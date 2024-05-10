"""create emploees table

Revision ID: 2827f7950baf
Revises: 
Create Date: 2024-05-01 21:00:56.925464

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2827f7950baf'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('employees',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=True),
    sa.Column('usersurname', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('sallary_usd', sa.Float(), nullable=True),
    sa.Column('next_sallary_raise', sa.Date(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_employees_email'), 'employees', ['email'], unique=True)
    op.create_index(op.f('ix_employees_next_sallary_raise'), 'employees', ['next_sallary_raise'], unique=False)
    op.create_index(op.f('ix_employees_sallary_usd'), 'employees', ['sallary_usd'], unique=False)
    op.create_index(op.f('ix_employees_username'), 'employees', ['username'], unique=False)
    op.create_index(op.f('ix_employees_usersurname'), 'employees', ['usersurname'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_employees_usersurname'), table_name='employees')
    op.drop_index(op.f('ix_employees_username'), table_name='employees')
    op.drop_index(op.f('ix_employees_sallary_usd'), table_name='employees')
    op.drop_index(op.f('ix_employees_next_sallary_raise'), table_name='employees')
    op.drop_index(op.f('ix_employees_email'), table_name='employees')
    op.drop_table('employees')
    # ### end Alembic commands ###