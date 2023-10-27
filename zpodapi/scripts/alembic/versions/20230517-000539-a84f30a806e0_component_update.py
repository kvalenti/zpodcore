"""component-update

Revision ID: a84f30a806e0
Revises: b3578d275fe2
Create Date: 2023-05-17 00:05:39.593858

"""
import sqlalchemy as sa
import sqlmodel
from alembic import op

# revision identifiers, used by Alembic.
revision = "a84f30a806e0"
down_revision = "b3578d275fe2"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "components",
        sa.Column("download_status", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    )
    op.drop_column("components", "enabled")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "components",
        sa.Column("enabled", sa.BOOLEAN(), autoincrement=False, nullable=False),
    )
    op.drop_column("components", "download_status")
    # ### end Alembic commands ###
