"""create users table

Revision ID: 0001_create_users
Revises: 
Create Date: 2026-11-26
"""
from alembic import op
import sqlalchemy as sa

revision = "0001_create_users"
down_revision = None
branch_labels = None
depends_on = None

def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), primary_key=True, index=True),
        sa.Column("name", sa.String(length=100), nullable=False),
        sa.Column("email", sa.String(length=255), nullable=False, unique=True, index=True),
        sa.Column("password", sa.String(length=255), nullable=False),
    )

def downgrade() -> None:
    op.drop_table("users")
