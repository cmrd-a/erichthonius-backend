"""init

Revision ID: 6312e2ecbbd6
Revises: 
Create Date: 2020-02-22 19:11:15.665187

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '6312e2ecbbd6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'schedule_file',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('year', sa.SmallInteger),
        sa.Column('semester', sa.SmallInteger),
        sa.Column('institute', sa.String(128)),
        sa.Column('grade', sa.String(1)),
        sa.Column('course', sa.SmallInteger),
        sa.Column('category', sa.String(16)),
        sa.Column('file_path', sa.String, nullable=False),
    )

    op.create_table(
        'group',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String, unique=True),
    )

    op.create_table(
        'room',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String, unique=True),
    )

    op.create_table(
        'teacher',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String, unique=True),
    )

    op.create_table(
        'period',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('file_id',
                  sa.Integer,
                  sa.ForeignKey('schedule_file.id', ondelete='CASCADE'),
                  nullable=False),
        sa.Column('day', sa.SmallInteger, nullable=False),
        sa.Column('number', sa.SmallInteger, nullable=False),
        sa.Column('even', sa.SmallInteger, nullable=False),
        sa.Column('name', sa.String),
        sa.Column('category', sa.String),

        sa.Column('group_id',
                  sa.Integer,
                  sa.ForeignKey('group.id', ondelete='CASCADE'),
                  nullable=False),
        sa.Column('room_id',
                  sa.Integer,
                  sa.ForeignKey('room.id', ondelete='CASCADE')),
        sa.Column('teacher_id',
                  sa.Integer,
                  sa.ForeignKey('teacher.id', ondelete='CASCADE')),

    )



def downgrade():
    pass
